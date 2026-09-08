#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, os, re, shutil, subprocess, time
from pathlib import Path

BASE = Path("/Users/sym/code/rubber-stamp-world-cities")
OUT_DIR = BASE / "images" / "poetry"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS = json.loads((BASE / "prompts_poetry.json").read_text(encoding="utf-8"))

def generate_one(item):
    target = BASE / item["output"]
    if target.exists() and target.stat().st_size > 100_000:
        print(f"[{item['id']}/50: {item['name']}] Already exists ({target.stat().st_size} bytes), skipping.", flush=True)
        return True

    print(f"\n--- [{item['id']}/50] Generating {item['name']} ({item['author']}) ---", flush=True)
    cmd = [
        "opencli", "gemini", "image", item["prompt"],
        "--window", "background",
        "-f", "yaml", "--op", str(OUT_DIR), "--timeout", "120"
    ]

    for attempt in range(1, 4):
        start_ts = time.time()
        try:
            print(f"  Attempt {attempt} running opencli gemini...", flush=True)
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=140)
            combined = r.stdout + "\n" + r.stderr

            # 1. Parse file from stdout
            found = re.findall(r"file:\s*📁\s*(\S+\.png)", combined)
            if found:
                saved = Path(os.path.expanduser(found[-1]))
                if saved.exists() and saved.stat().st_size > 100_000:
                    if saved.resolve() != target.resolve():
                        shutil.move(str(saved), str(target))
                    print(f"  SUCCESS (parsed): saved to {target.name} ({target.stat().st_size} bytes)", flush=True)
                    return True

            # 2. Check OUT_DIR for new gemini_*.png
            new_files = [p for p in OUT_DIR.glob("gemini_*.png") if p.stat().st_mtime >= start_ts - 5 and p.stat().st_size > 100_000]
            if new_files:
                new_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
                shutil.move(str(new_files[0]), str(target))
                print(f"  SUCCESS (fs scan): saved to {target.name} ({target.stat().st_size} bytes)", flush=True)
                return True

            print(f"  Attempt {attempt} output:\n{combined[-250:]}", flush=True)
        except Exception as e:
            print(f"  Attempt {attempt} error: {e}", flush=True)
        time.sleep(3)

    print(f"[{item['name']}] FAILED after 3 attempts.", flush=True)
    return False

def main():
    print(f"=== Starting Poetry Stamp Generation with Gemini ({len(PROMPTS)} items) ===", flush=True)
    for item in PROMPTS:
        generate_one(item)
        time.sleep(2)
    print("\n=== All Poetry stamps generated! ===", flush=True)

if __name__ == "__main__":
    main()
