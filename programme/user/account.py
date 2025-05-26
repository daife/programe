import json
import os

# 获取当前脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建绝对路径
USER_DATA_FILE = os.path.join(SCRIPT_DIR, "user_data.json")

# 初始化数据文件
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

# 加载用户数据
def load_users():
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存用户数据
def save_users(users):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

# 注册
def register():
    users = load_users()
    username = input("请输入新用户名：").strip()
    if username in users:
        print("用户名已存在，请重新输入。")
        return None
    password = input("请输入密码：").strip()
    users[username] = {"password": password}
    save_users(users)
    print(f"✅ 注册成功，欢迎你 {username}！")
    return username

# 登录
def login():
    users = load_users()
    username = input("请输入用户名：").strip()
    if username not in users:
        print("用户名不存在。")
        return None
    password = input("请输入密码：").strip()
    if users[username]["password"] != password:
        print("密码错误。")
        return None
    print(f"✅ 登录成功，欢迎回来 {username}！")
    return username
