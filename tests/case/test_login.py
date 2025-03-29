# 编写一个简单的登录程序的测试脚本

from src.login.slap_that_like_button import login  # 导入登录函数

# 定义登录测试类
class TestLogin:
    # 定义登录测试方法
    def test_login_success(self):
        # 打印登录信息
        print("登录测试用例 - 成功")
        # 调用登录函数并断言结果
        assert login("admin", "password") == True

    def test_login_failure(self):
        # 打印登录信息
        print("登录测试用例 - 失败")
        # 调用登录函数并断言结果
        assert login("wrong_user", "wrong_password") == False