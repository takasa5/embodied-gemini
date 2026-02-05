#!/usr/bin/env venv/bin/python

import sys
import os
from datetime import datetime

# Get the directory where memory.txt will be stored
script_dir = os.path.dirname(os.path.abspath(__file__))
memory_dir = os.path.join(script_dir, '..', '..', '..', 'memory')
memory_file_path = os.path.join(memory_dir, 'memory.txt')

def memorize(text):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(memory_file_path), exist_ok=True)
        with open(memory_file_path, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {text}\n")
        print(f"記憶しました: {text}")
    except Exception as e:
        print(f"記憶に失敗しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_to_memorize = sys.argv[1]
        memorize(text_to_memorize)
    else:
        print("使用法: memorize.py <記憶するテキスト>", file=sys.stderr)
        sys.exit(1)
