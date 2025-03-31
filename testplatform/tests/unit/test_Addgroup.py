import requests
import unittest

class TestAddgroup(unittest.TestCase):
    def test_addgroup_sucess_001(self):
        response = requests.post('http://127.0.0.1:8000/home/api/groups/addgroup/', json={
  "name": "Python 学习小组",
  "description": "这是一个学习 Python 的小组。",
  "created_by": 1 
})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
    "ret": 0,
    "msg": "小组创建成功."
})

    def test_addgroup_failure_001(self):
        response = requests.post('http://127.0.0.1:8000/home/api/groups/addgroup/', json={
  "name": "Python 学习小组",
  "description": "这是一个学习 Python 的小组。",
  "created_by": 3  
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "创建者不存在."
})

    def test_addgroup_failure_002(self):
        response = requests.post('http://127.0.0.1:8000/home/api/groups/addgroup/', json={
  "description": "这是一个学习 Python 的小组。",
  "created_by": 1  
})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "创建者不存在."
})

    def test_addgroup_failure_003(self):
        response = requests.post('http://127.0.0.1:8000/home/api/groups/addgroup/', json={
  "name": "Python 学习小组",
  "created_by": 1 
})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Error: NOT NULL constraint failed: Login_studygroup.description"
})

    def test_addgroup_failure_004(self):
        response = requests.post('http://127.0.0.1:8000/home/api/groups/addgroup/', json={
  "name": "Python 学习小组",
  "description": "这是一个学习 Python 的小组。",
})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {
    "ret": 1,
    "msg": "Invalid JSON format."
})

if __name__ == '__main__':
    unittest.main()
