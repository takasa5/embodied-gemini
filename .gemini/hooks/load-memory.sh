#!/bin/bash

memory=$(cat "$(dirname "$0")/../memory/memory.txt")

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "BeforeAgent",
    "additionalContext": "記憶（**毎回参照する**）:\n$memory"
  }
}
EOF