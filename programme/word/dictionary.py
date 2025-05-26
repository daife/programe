import json
import os

# 获取当前脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建绝对路径
WORDBANK_FILE = os.path.join(SCRIPT_DIR, "wordbank.json")

# 加载词库
def load_wordbank():
    if not os.path.exists(WORDBANK_FILE):
        print("词库文件不存在！")
        return []
    with open(WORDBANK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 查询某个单词
def lookup(word, wordbank):
    for entry in wordbank:
        if entry["word"].lower() == word.lower():
            return entry
    return None
