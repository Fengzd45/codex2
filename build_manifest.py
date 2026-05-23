import os

def generate_manifest():
    base_dir = "资料"
    manifest = []

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.pdf', '.mp4', '.txt')):
                full_path = os.path.join(root, file)
                manifest.append(full_path)

    # 写入JSON（你之前的功能）
    with open("file_manifest.json", "w", encoding="utf-8") as f:
        import json
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # 新增：写入TXT，覆盖旧的文件清单.txt
    with open("文件清单.txt", "w", encoding="utf-8") as f:
        for path in manifest:
            f.write(path + "\n")

    print(f"✅ 完成！共 {len(manifest)} 人有资料")

if __name__ == "__main__":
    generate_manifest()
