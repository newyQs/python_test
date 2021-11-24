import unittest
from login import app
import json


class TestLogin(unittest.TestCase):
    """定义测试案例"""

    def setUp(self):
        """在执行具体的测试方法前，先被调用"""

        self.app = app
        # 激活测试标志
        app.config['TESTING'] = True

        # 可以使用python的http标准客户端进行测试
        # urllib  urllib2  requests

        # 在这里,使用flask提供的测试客户端进行测试
        self.client = app.test_client()

    def test_empty_name_password(self):
        """测试模拟场景，用户名或密码不完整"""
        # 使用客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/login", data={})
        # respoonse.data是响应体数据
        resp_json = response.data
        # 按照json解析
        resp_dict = json.loads(resp_json)
        # 使用断言进行验证：是否存在code字符串在字典中
        self.assertIn("code", resp_dict)
        # 获取code的返回码的值，验证是否为错误码 65535
        code = resp_dict.get("code")
        self.assertEqual(code, 65535)

        # 测试只传name
        response = self.client.post("/login", data={"name": "admin"})
        # respoonse.data是响应体数据
        resp_json = response.data
        # 按照json解析
        resp_dict = json.loads(resp_json)
        # 使用断言进行验证
        self.assertIn("code", resp_dict)
        # 验证错误码 65535
        code = resp_dict.get("code")
        self.assertEqual(code, 65535)
        # 验证返回信息
        msg = resp_dict.get('message')
        self.assertEqual(msg, "参数不完整")

    def test_wrong_name_password(self):
        """测试用户名或密码错误"""
        # 使用客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/login", data={"name": "admin", "password": "123456789"})
        # respoonse.data是响应体数据
        resp_json = response.data
        # 按照json解析
        resp_dict = json.loads(resp_json)
        # 使用断言进行验证
        self.assertIn("code", resp_dict)
        # 验证错误码
        code = resp_dict.get("code")
        self.assertEqual(code, 65535)
        # 验证返回信息
        msg = resp_dict.get('message')
        self.assertEqual(msg, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main()
