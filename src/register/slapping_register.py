#添加一个注册功能用于测试

def register(username, password, email):
    if username is None or password is None or email is None:
        return False
    # 这里可以添加实际的注册逻辑
    if username and password and email:
        # 假设注册成功，返回True
        return True
    return False