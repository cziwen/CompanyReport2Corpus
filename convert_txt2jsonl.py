import os
import glob
import json
import argparse

def collect_txt_files(folders):
    """从多个文件夹中收集所有 .txt 文件路径"""
    all_txt_files = []
    for folder in folders:
        txt_files = glob.glob(os.path.join(folder, "*.txt"))
        all_txt_files.extend(txt_files)
    return all_txt_files

def convert_to_jsonl(txt_files, output_path):
    """将每个 .txt 文件写入 JSONL 文件中，每个文件一条记录"""
    with open(output_path, "w", encoding="utf-8") as fout:
        for path in txt_files:
            try:
                with open(path, "r", encoding="utf-8") as fin:
                    content = fin.read().strip()
                    if content:  # 跳过空文件
                        fout.write(json.dumps({"text": content}) + "\n")
            except Exception as e:
                print(f"Failed to process {path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .txt files from multiple folders to JSONL format.")
    parser.add_argument(
        "--folders", "-f",
        nargs="+",
        required=True,
        help="List of folders containing .txt files"
    )
    parser.add_argument(
        "--output", "-o",
        default="output.jsonl",
        help="Output JSONL file path (default: output.jsonl)"
    )
    args = parser.parse_args()

    txt_files = collect_txt_files(args.folders)
    print(f"Found {len(txt_files)} .txt files.")
    convert_to_jsonl(txt_files, args.output)
    print(f"✅ Done! Output saved to {args.output}")