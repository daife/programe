from user.account import login, register
from word.dictionary import load_wordbank
from practice.spell_check import spelling_test
from practice.meaning_check import meaning_test
from stats.record import save_result
import os
import json

def login_menu():
    while True:
        print("\n=== 欢迎使用背单词软件 ===")
        print("1. 登录")
        print("2. 注册")
        print("3. 退出")
        choice = input("请选择（1/2/3）：").strip()

        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            user = register()
            if user:
                return user
        elif choice == "3":
            print("再见！")
            exit()
        else:
            print("❌ 输入无效，请重新选择。")

def main_menu(username):
    wordbank = load_wordbank()

    while True:
        print(f"\n=== 主菜单 - 当前用户：{username} ===")
        print("1. 拼写测试（中文 → 英文）")
        print("2. 释义测试（英文 → 中文）")
        print("3. 查看练习记录")
        print("4. 退出登录")

        choice = input("请选择功能（1-4）：").strip()

        if choice == "1":
            result = spelling_test(wordbank)
            save_result(username, "spelling", result)
        elif choice == "2":
            result = meaning_test(wordbank)
            save_result(username, "meaning", result)
        elif choice == "3":
            show_user_record(username)
        elif choice == "4":
            print("已退出登录。\n")
            break
        else:
            print("❌ 无效输入，请重试。")

# 暂时简单显示统计（下步可改进）
def show_user_record(username):
    from stats import record
    path = os.path.join(record.RECORD_DIR, f"{username}.json")
    if not os.path.exists(path):
        print("暂无记录。")
        return

    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)  # 修复之前的错误

    print(f"\n📊 用户 {username} 的练习记录：")
    for entry in records:
        correct = sum(1 for item in entry["result"] if item[1])
        total = len(entry["result"])
        print(f"- [{entry['time']}] 类型：{entry['type']}，正确率：{correct}/{total}")

if __name__ == "__main__":
    while True:
        user = login_menu()
        main_menu(user)

