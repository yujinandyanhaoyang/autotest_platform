import requests
import unittest

class TestNewregister(unittest.TestCase):
    def test_register_sucess_001(self):
        response = requests.post('http://127.0.0.1:8000/home/api/register/', json= { "username": "userfour",
  "email": "user.four@example.com",
  "password": "anotherPass123"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
    "ret": 0,
    "msg": "User registered successfully."
})

    def test_register_failure_001(self):
        response = requests.post('http://127.0.0.1:8000/home/api/register/', json= { 
  "email": "user.four1@example.com",
  "password": "anotherPass124"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Registration failed: 'NoneType' object has no attribute 'lower'"
})

    def test_register_failure_002(self):
        response = requests.post('http://127.0.0.1:8000/home/api/register/', json= { "username": "userfour",
  "password": "anotherPass125"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Username, Email and password are required."
})

    def test_register_failure_004(self):
        response = requests.post('http://127.0.0.1:8000/home/api/register/', json= { "username": "userfour",
  "email": "user.four1@example.com",
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Registration failed: Expecting property name enclosed in double quotes: line 5 column 1 (char 69)"
})

    def test_register_failure_005(self):
        response = requests.post('http://127.0.0.1:8000/home/ahttp://127.0.0.1:8000/home/api/register/pi/register/', json= { "username": "userfour",
  "email": "user.four@example.com",
  "password": "anotherPass128"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Username or Email already exists."
})

if __name__ == '__main__':
    unittest.main()
