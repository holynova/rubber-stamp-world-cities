from pathlib import Path
import json, os, re, shutil, subprocess, time

BASE = Path(__file__).parent
IMAGE_DIR = BASE / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)
items = json.loads((BASE / "prompts.json").read_text(encoding="utf-8"))
log_path = BASE / "batch.log"
manifest_path = BASE / "generation_manifest.json"
manifest = {}
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

env = os.environ.copy()
records = []
for item in items:
    idx = item["id"]
    target = BASE / item["output"]
    if target.exists() and target.stat().st_size > 100_000:
        records.append({"id": idx, "city": item["city"], "status": "existing", "file": str(target)})
        continue
    started = time.strftime("%Y-%m-%d %H:%M:%S")
    cmd = [
        "opencli", "chatgpt", "image", item["prompt"],
        "--window", "background", "--site-session", "persistent",
        "-f", "yaml", "--op", str(IMAGE_DIR), "--timeout", "240",
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=360, env=env)
        combined = r.stdout + "\n" + r.stderr
        found = re.findall(r"file:\s*📁\s*(\S+\.png)", combined)
        saved = None
        if found:
            saved = Path(found[-1]).expanduser()
            if saved.exists() and saved.stat().st_size > 100_000:
                shutil.copy2(saved, target)
        ok = target.exists() and target.stat().st_size > 100_000
        rec = {"id": idx, "city": item["city"], "status": "success" if ok else "failed", "returncode": r.returncode, "file": str(target) if ok else None, "raw_file": str(saved) if saved else None, "started": started, "stdout_tail": combined[-1200:]}
    except Exception as e:
        rec = {"id": idx, "city": item["city"], "status": "error", "error": repr(e), "started": started}
    records.append(rec)
    manifest[str(idx)] = rec
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if idx != items[-1]["id"]:
        time.sleep(60)

print(json.dumps({"total": len(items), "success": sum(1 for x in records if x.get("status") in ("success", "existing")), "failed": sum(1 for x in records if x.get("status") not in ("success", "existing")), "records": records}, ensure_ascii=False))
