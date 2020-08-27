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
        self.assertEqual(t[1],'421847541@qq.com')

