from pathlib import Path
import shutil, json, csv
from PIL import Image, ImageDraw, ImageFont

base = Path(__file__).parent
images = base / "images"
source = images / "chatgpt_1788332035255.png"
target = images / "26_利马.png"
if source.exists() and not target.exists():
    shutil.copy2(source, target)

items = json.loads((base / "prompts.json").read_text(encoding="utf-8"))
manifest = json.loads((base / "generation_manifest.json").read_text(encoding="utf-8")) if (base / "generation_manifest.json").exists() else {}
manifest["1"] = {"id": 1, "city": "上海", "status": "success", "file": str(images / "01_上海.png"), "raw_file": str(images / "chatgpt_1788327240671.png")}
manifest["26"] = {"id": 26, "city": "利马", "status": "success", "file": str(target), "raw_file": str(source)}
(base / "generation_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

rows = []
for item in items:
    path = base / item["output"]
    with Image.open(path) as im:
        rows.append([item["id"], item["city"], item["output"], f"{im.width}x{im.height}", path.stat().st_size])
with (base / "mapping.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["编号", "城市", "文件", "尺寸", "字节数"])
    writer.writerows(rows)

font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 26)
thumbs = []
for item in items:
    with Image.open(base / item["output"]).convert("RGB") as im:
        im.thumbnail((240, 300))
        card = Image.new("RGB", (280, 350), (238, 229, 213))
        card.paste(im, ((280 - im.width) // 2, 8))
        ImageDraw.Draw(card).text((14, 315), f"{item['id']:02d}  {item['city']}", font=font, fill=(41, 39, 34))
        thumbs.append(card)
sheet = Image.new("RGB", (1400, 2100), (226, 215, 196))
for i, thumb in enumerate(thumbs):
    sheet.paste(thumb, ((i % 5) * 280, (i // 5) * 350))
contact = base / "contact_sheet" / "world-cities-contact-sheet.jpg"
contact.parent.mkdir(exist_ok=True)
sheet.save(contact, quality=92)

invalid = []
for row in rows:
    path = base / row[2]
    with Image.open(path) as im:
        if im.size != (1122, 1402) or row[4] < 100000:
            invalid.append(row)
print(json.dumps({"images": len(rows), "invalid": invalid, "contact_sheet": str(contact), "mapping": str(base / 'mapping.csv')}, ensure_ascii=False))
