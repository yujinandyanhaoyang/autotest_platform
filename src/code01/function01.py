# 添加一个登录功能
def login(username, password):
    """
    登录功能

    参数:
    - username (str): 用户名
    - password (str): 密码

    返回值:
    - bool: 登录成功返回True，登录失败返回False
    """
    # 假设已经注册的记录为
    records = [
        {"username": "user1", "password": "pass1"},
        {"username": "user2", "password": "pass2"},
        {"username": "user3", "password": "pass3"},
    ]
    for record in records:
        if record["username"] == username and record["password"] == password:
            return True
    # 假设输入的密码不正确，则返回
    return False
