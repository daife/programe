import json
import os

# 获取当前脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 构建绝对路径
USER_DATA_FILE = os.path.join(SCRIPT_DIR, "user_data.json")

# 加载用户数据（如果没有就创建一个空文件）
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f)
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存用户数据
def save_user_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# 注册新用户
def register(username, password):
    data = load_user_data()
    if username in data:
        print("用户名已存在！")
        return False
    data[username] = {
        "password": password,
        "progress": {
            "word_count": 0,
            "correct_answers": 0,
            "wrong_answers": 0,
            "last_practice": None
        }
    }
    save_user_data(data)
    print(f"用户 {username} 注册成功！")
    return True

# 登录验证
def login(username, password):
    data = load_user_data()
    if username not in data:
        print("用户名不存在！")
        return None
    if data[username]["password"] != password:
        print("密码错误！")
        return None
    print(f"欢迎回来，{username}！")
    return data[username]
