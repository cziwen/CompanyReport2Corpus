# token_counter.py

import os
import glob
import argparse
import config

import tiktoken

def count_tokens_in_file(file_path: str, encoder) -> int:
    """读取文件并返回其 token 数量。"""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(encoder.encode(text))

def main():
    parser = argparse.ArgumentParser(description="统计目录下所有 .txt 文件的 token 数量")
    parser.add_argument(
        "--folder", "-f",
        default=config.OUTPUT_DIR,
        help="要统计的文本文件目录（默认: output/corpus）"
    )
    parser.add_argument(
        "--model", "-m",
        default="gpt-4",
        help="用于编码的模型名称（tiktoken 支持的模型）"
    )
    args = parser.parse_args()

    # 初始化 tokenizer
    try:
        encoder = tiktoken.encoding_for_model(args.model)
    except KeyError:
        # 如果指定模型不可用，则退回到默认编码
        encoder = tiktoken.get_encoding("cl100k_base")
        print(f"警告：模型 {args.model} 未识别，使用 cl100k_base 编码。")

    pattern = os.path.join(args.folder, "*.txt")
    files = glob.glob(pattern)
    if not files:
        print(f"未在目录 {args.folder} 找到任何 .txt 文件。")
        return

    total_tokens = 0
    for file_path in sorted(files):
        count = count_tokens_in_file(file_path, encoder)
        print(f"{os.path.basename(file_path)}: {count} tokens")
        total_tokens += count

    print(f"\n总 token 数量: {total_tokens}")

if __name__ == "__main__":
    main()