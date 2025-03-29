#测试注册功能
from src.register.slapping_register import register

class TestRegister:
    def test_register_success(self):
        # 测试注册成功的情况
        assert register("newuser", "newpassword", "newemail") == True

    def test_register_noname(self):#不输入用户名
        # 测试注册失败的情况
        assert register(None, "newpassword", "newemail") == False

    def test_register_nonepassword(self):#不输入密码
        # 测试注册失败的情况
        assert register("newuser", None, "newemail") == False

    def test_register_noemail(self):#不输入邮箱
        # 测试注册失败的情况
        assert register("newuser", "newpassword", None) == False
    def test_register_multiple_none(self):
        # 测试多个参数为 None 的情况
        assert register(None, None, "newemail") == False
        assert register(None, "newpassword", None) == False
        assert register("newuser", None, None) == False
        assert register(None, None, None) == False
    def test_register_empty_strings(self):
        # 测试空字符串的情况
        assert register("", "newpassword", "newemail") == False
        assert register("newuser", "", "newemail") == False
        assert register("newuser", "newpassword", "") == False

