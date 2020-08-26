3# -*- coding:utf-8 -*-
import unittest
import json
import requests
from common import demo
from common.LG import LG
class Login_001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = requests.session()
        cls.lg = LG(s)
    def test_login(self):
        t = self.lg.login('421847541@qq.com','12345678q')
        self.assertEqual(t[0],'421847541@qq.com')

