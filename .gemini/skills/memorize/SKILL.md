---
name: memorize
description: 会話の履歴や重要な情報を記憶し、後で参照できるようにするスキルです。永続的な記憶が必要な時や、特定の情報を忘れないようにしたい時に使用します。
---

# Memorize

## Overview

このスキルは、エージェントがユーザーとの会話の中で得た情報や、自身が記憶しておくべきと判断した内容を永続的に記録することを可能にします。記録された情報は、後で必要になった際にいつでも参照することができます。情報はタイムスタンプ付きで `.gemini/memory/memory.txt` に追記形式で保存されます。

## スキルの使用方法

このスキルは、以下の2つのスクリプトを通じて利用できます。

### `memorize.py` (記憶する)

指定されたテキスト情報を記憶ファイル (`.gemini/memory/memory.txt`) にタイムスタンプ付きで追記します。

**使用法:**
```bash
run_shell_command("venv/bin/python .gemini/skills/memorize/scripts/memorize.py \"記憶したいテキスト\"")
```

**例:**
```bash
run_shell_command("venv/bin/python .gemini/skills/memorize/scripts/memorize.py \"ユーザーはMacBookを使用しています\"")
```

### `recall.py` (思い出す)

記憶ファイル (`.gemini/memory/memory.txt`) に保存されている全ての情報を読み込み、出力します。

**使用法:**
```bash
run_shell_command("venv/bin/python .gemini/skills/memorize/scripts/recall.py")
```

**例:**
```bash
run_shell_command("venv/bin/python .gemini/skills/memorize/scripts/recall.py")
```

## Resources

このスキルには、以下のスクリプトが含まれています。

### scripts/
特定の操作を実行するために直接実行できるコードです。

*   `memorize.py`: テキスト情報を記憶ファイルに追記します。
*   `recall.py`: 記憶ファイルから情報を読み込み、出力します。
