import os
import glob
import argparse
import config
import tiktoken
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

def count_tokens_in_file(file_path: str, encoder_name: str) -> tuple:
    """读取文件并返回文件名和其 token 数量。"""
    encoder = tiktoken.get_encoding(encoder_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    count = len(encoder.encode(text))
    return os.path.basename(file_path), count

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
    parser.add_argument(
        "--workers", "-w",
        type=int,
        default=os.cpu_count(),
        help="并行进程数，默认使用所有核心"
    )
    args = parser.parse_args()

    # 初始化编码器名称（避免序列化 encoder 对象）
    try:
        encoder = tiktoken.encoding_for_model(args.model)
        encoder_name = encoder.name
    except KeyError:
        encoder_name = "cl100k_base"
        print(f"警告：模型 {args.model} 未识别，使用 cl100k_base 编码。")

    # 查找文件
    pattern = os.path.join(args.folder, "*.txt")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"未在目录 {args.folder} 找到任何 .txt 文件。")
        return

    total_tokens = 0
    results = []

    # 并发处理文件
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(count_tokens_in_file, fp, encoder_name): fp for fp in files}
        for future in tqdm(as_completed(futures), total=len(futures), desc="统计中"):
            filename, count = future.result()
            # print(f"{filename}: {count} tokens")
            total_tokens += count

    print(f"\n总 token 数量: {total_tokens}")

if __name__ == "__main__":
    main()