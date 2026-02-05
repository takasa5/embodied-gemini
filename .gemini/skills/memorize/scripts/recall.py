#!/usr/bin/env venv/bin/python

import sys
import os

# Get the directory where memory.txt is stored
script_dir = os.path.dirname(os.path.abspath(__file__))
memory_dir = os.path.join(script_dir, '..', '..', '..', 'memory')
memory_file_path = os.path.join(memory_dir, 'memory.txt')

def recall():
    try:
        if not os.path.exists(memory_file_path):
            print("記憶された情報はありません。", file=sys.stderr)
            return

        with open(memory_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                print("記憶された情報:\n" + content.strip())
            else:
                print("記憶された情報はありません。", file=sys.stderr)
    except Exception as e:
        print(f"記憶の読み込みに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    recall()
