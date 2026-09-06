#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import json, os, re, shutil, subprocess, time

BASE = Path(__file__).parent
ZODIAC_DIR = BASE / "images" / "zodiac"
SOLAR_DIR = BASE / "images" / "solar_terms"
KAMA_DIR = BASE / "images" / "kama_sutra"
ZODIAC_DIR.mkdir(parents=True, exist_ok=True)
SOLAR_DIR.mkdir(parents=True, exist_ok=True)
KAMA_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS_ZODIAC = json.loads((BASE / "prompts_zodiac.json").read_text(encoding="utf-8")) if (BASE / "prompts_zodiac.json").exists() else []
PROMPTS_SOLAR = json.loads((BASE / "prompts_solar_terms.json").read_text(encoding="utf-8")) if (BASE / "prompts_solar_terms.json").exists() else []
PROMPTS_KAMA = json.loads((BASE / "prompts_kama_sutra.json").read_text(encoding="utf-8")) if (BASE / "prompts_kama_sutra.json").exists() else []

def wait_for_session_ready(timeout=60):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = subprocess.run(["opencli", "chatgpt", "status", "-f", "yaml"], capture_output=True, text=True, timeout=10)
            if "SESSION_BUSY" not in (r.stdout + r.stderr):
                return True
        except Exception:
            return True
        time.sleep(5)
    return False

def generate_item(item, out_dir):
    target = BASE / item["output"]
    if target.exists() and target.stat().st_size > 100_000:
        print(f"[{item['name']}] Already exists: {target.name} ({target.stat().st_size} bytes)", flush=True)
        return True

    print(f"[{item['name']}] Starting generation...", flush=True)
    env = os.environ.copy()
    
    cmd = [
        "opencli", "chatgpt", "image", item["prompt"],
        "--window", "background",
        "-f", "yaml", "--op", str(out_dir), "--timeout", "240"
    ]
    
    for attempt in range(1, 6):
        wait_for_session_ready()
        start_ts = time.time()
        try:
            print(f"  [{item['name']}] Running opencli (attempt {attempt})...", flush=True)
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=280, env=env)
            combined = r.stdout + "\n" + r.stderr
            
            if "SESSION_BUSY" in combined:
                print(f"  [{item['name']}] Session busy, waiting 15s...", flush=True)
                time.sleep(15)
                continue
            
            # 1. Parse output file from stdout
            found = re.findall(r"file:\s*📁\s*(\S+\.png)", combined)
            if found:
                saved = Path(os.path.expanduser(found[-1]))
                if saved.exists() and saved.stat().st_size > 100_000:
                    if saved.resolve() != target.resolve():
                        shutil.move(str(saved), str(target))
                    print(f"  [{item['name']}] SUCCESS (parsed): saved to {target.name} ({target.stat().st_size} bytes)", flush=True)
                    return True
            
            # 2. Check out_dir for newly created chatgpt_*.png
            new_files = [p for p in out_dir.glob("chatgpt_*.png") if p.stat().st_mtime >= start_ts - 5 and p.stat().st_size > 100_000]
            if new_files:
                new_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
                shutil.move(str(new_files[0]), str(target))
                print(f"  [{item['name']}] SUCCESS (fs scan): saved to {target.name} ({target.stat().st_size} bytes)", flush=True)
                return True
                
            print(f"  [{item['name']}] Attempt {attempt} output:\n{combined[-300:]}", flush=True)
        except subprocess.TimeoutExpired:
            print(f"  [{item['name']}] Attempt {attempt} timeout (280s).", flush=True)
        except Exception as e:
            print(f"  [{item['name']}] Attempt {attempt} exception: {e}", flush=True)
        time.sleep(8)
    
    print(f"[{item['name']}] FAILED after all attempts.", flush=True)
    return False

def run_all(task="all"):
    manifest_path = BASE / "generation_manifest_series.json"
    manifest = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}

    if task in ("all", "zodiac"):
        print(f"=== Generating Zodiac Series ({len(PROMPTS_ZODIAC)} items) ===", flush=True)
        for idx, item in enumerate(PROMPTS_ZODIAC, 1):
            target = BASE / item["output"]
            if target.exists() and target.stat().st_size > 100_000:
                continue
            print(f"\n--- Zodiac [{idx}/{len(PROMPTS_ZODIAC)}]: {item['name']} ---", flush=True)
            ok = generate_item(item, ZODIAC_DIR)
            manifest[item["output"]] = {
                "name": item["name"],
                "series": "zodiac",
                "output": item["output"],
                "status": "success" if ok else "failed",
                "time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(6)

    if task in ("all", "solar"):
        print(f"\n=== Generating Solar Terms Series ({len(PROMPTS_SOLAR)} items) ===", flush=True)
        # Loop until all solar terms are generated
        while True:
            missing = [item for item in PROMPTS_SOLAR if not (BASE / item["output"]).exists() or (BASE / item["output"]).stat().st_size <= 100_000]
            if not missing:
                print("\n All 24 Solar Terms generated successfully!", flush=True)
                break
            
            print(f"\n--- Remaining Solar Terms to generate: {len(missing)} items ---", flush=True)
            for idx, item in enumerate(missing, 1):
                print(f"\n--- Solar Term ({idx}/{len(missing)}): {item['name']} ---", flush=True)
                ok = generate_item(item, SOLAR_DIR)
                manifest[item["output"]] = {
                    "name": item["name"],
                    "series": "solar_terms",
                    "output": item["output"],
                    "status": "success" if ok else "failed",
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
                time.sleep(6)

    if task in ("all", "kama", "kama_sutra"):
        print(f"\n=== Generating Kama Sutra Series ({len(PROMPTS_KAMA)} items) ===", flush=True)
        while True:
            missing = [item for item in PROMPTS_KAMA if not (BASE / item["output"]).exists() or (BASE / item["output"]).stat().st_size <= 100_000]
            if not missing:
                print("\n All 10 Kama Sutra prints generated successfully!", flush=True)
                break
            
            print(f"\n--- Remaining Kama Sutra prints to generate: {len(missing)} items ---", flush=True)
            for idx, item in enumerate(missing, 1):
                print(f"\n--- Kama Sutra ({idx}/{len(missing)}): {item['name']} ---", flush=True)
                ok = generate_item(item, KAMA_DIR)
                manifest[item["output"]] = {
                    "name": item["name"],
                    "series": "kama_sutra",
                    "output": item["output"],
                    "status": "success" if ok else "failed",
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
                time.sleep(6)

    print("\n=== Generation Batch Finished ===", flush=True)

if __name__ == "__main__":
    import sys
    task_arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    run_all(task_arg)
