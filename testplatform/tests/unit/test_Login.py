import requests
import unittest

class TestLogin(unittest.TestCase):
    def test_login_sucess_001(self):
        response = requests.get('http://127.0.0.1:8000/home/api/login/', params={
    "username_or_email": "testuser",
    "password": "testpassword"
})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
    "ret": 0,
    "msg": "登录成功。"
})

    def test_login_failure_001(self):
        response = requests.get('http://127.0.0.1:8000/home/api/login/', params={
    "password": "testpassword"
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "用户名/邮箱和密码是必需的。"
})

    def test_login_failure_002(self):
        response = requests.get('http://127.0.0.1:8000/home/api/login/', params={
    "username_or_email": "erroruser",
    "password": "testpassword"
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "无效的用户名/邮箱或密码。"
})

    def test_login_failure_003(self):
        response = requests.get('http://127.0.0.1:8000/home/api/login/', params={
    "username_or_email": "testuser",
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "无效的 JSON 格式。"
})

    def test_login_failure_004(self):
        response = requests.get('http://127.0.0.1:8000/home/api/login/', params={
    "username_or_email": "testuser",
    "password": "erro"
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "无效的用户名/邮箱或密码。"
})

if __name__ == '__main__':
    unittest.main()
