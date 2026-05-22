import json
import os
from pathlib import Path

data_dir = Path("资料")
manifest = {}

if not data_dir.exists():
    print("找不到资料文件夹")
    exit(1)

for person_dir in data_dir.iterdir():
    if not person_dir.is_dir():
        continue
    person_name = person_dir.name
    files_list = []
    for file_path in person_dir.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext in ['.txt', '.jpg', '.jpeg', '.png', '.gif', '.mp3', '.wav', '.mp4', '.mov', '.webm']:
                files_list.append({
                    "name": file_path.name,
                    "path": f"资料/{person_name}/{file_path.name}",
                    "ext": ext[1:]
                })
    if files_list:
        manifest[person_name] = files_list
        print(f"✅ {person_name}: {len(files_list)} 个文件")

with open("file_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\n🎉 完成！共 {len(manifest)} 人有资料")
