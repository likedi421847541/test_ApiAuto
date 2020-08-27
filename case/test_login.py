3# -*- coding:utf-8 -*-
import unittest
import requests
from common.LG import LG
class Login_001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lg = LG()
    def test_login(self):
        t = self.lg.login('421847541@qq.com','12345678q')
        self.assertEqual(t['email'],'421847541@qq.com')
    def test_login_error(self):
        t = self.lg.login(password='123456')
        self.assertIn(t['message'],'The username or password is incorrect.')
