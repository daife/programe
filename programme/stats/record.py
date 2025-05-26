import json
import os
from datetime import datetime

# 获取当前脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建绝对路径
RECORD_DIR = os.path.join(SCRIPT_DIR, "user_records")

# 初始化目录
os.makedirs(RECORD_DIR, exist_ok=True)

# 保存测试结果
def save_result(username, test_type, result_list):
    record_file = os.path.join(RECORD_DIR, f"{username}.json")

    # 构造记录条目
    record_entry = {
        "type": test_type,  # spell 或 meaning
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": result_list  # [(word, True), (word, False)]
    }

    # 加载原有记录
    if os.path.exists(record_file):
        with open(record_file, "r", encoding="utf-8") as f:
            records = json.load(f)
    else:
        records = []

    records.append(record_entry)

    # 保存
    with open(record_file, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
