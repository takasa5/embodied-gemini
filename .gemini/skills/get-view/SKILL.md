---
name: get-view
description: "macOSのカメラからPythonスクリプト(capture_image.py)を使って画像をキャプチャし、それを読み込みます。スクリプトは現在の作業ディレクトリに存在する必要があります。"
---

# get-view スキル

## 説明

このスキルは、macOSのデフォルトカメラから単一の画像をキャプチャして利用可能にします。これは`opencv-python`を使用する外部Pythonスクリプト(`capture_image.py`)に依存しています。

## 前提条件

- ユーザーのPython環境に`opencv-python`がインストールされている必要があります (`pip install opencv-python`)。
- `capture_image.py`スクリプトが`.gemini/skills/get-view/scripts/`ディレクトリに存在する必要があります。

## 指示

このスキルが呼び出された場合、他のアクションを挟むことなく、この2段階のプロセスを単一の不可分な操作として厳密に従う必要があります。

1.  **画像のキャプチャとパスの取得:** まず、キャプチャスクリプトを実行して画像を保存し、そのパスを取得します。`run_shell_command`ツールを次のコマンドで使用してください：
    ```
    venv/bin/python .gemini/skills/get-view/scripts/capture_image.py --output_dir {project_temp_dir}
    ```
    このコマンドは、キャプチャされた画像の絶対パスを出力します。
    **注意:** `{project_temp_dir}`は、エージェントのコンテキストで提供される実際のプロジェクトの一時ディレクトリパスに置き換える必要があります。

2.  **画像データの読み込み:** パスを取得した直後に、そのパスを指定して`read_file`ツールを使用し、画像データを読み込みます。

**重要:** `read_file`ツールが画像コンテンツを正常に返すまで、景色の説明、分析、その他のコメントを試みないでください。上記2つのステップは連続して実行する必要があります。