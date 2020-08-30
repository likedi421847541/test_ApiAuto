# -*- coding:utf-8 -*-
import unittest
import requests
from common.LG import LG
class LGClass(unittest.TestCase):
    lg = LG()
    lg.login()  # 先登录获取 token 和 user_id
    center_id = lg.add_center()['id']  # 添加学校，获取学校 ID
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.g = globals() # 全局变量
    def tearDown(self):
        self.lg.del_class(self.g['id'])
    @classmethod
    def tearDownClass(cls):
        cls.lg.delete_centers(cls.center_id)
    def test_add_class(self):
        addClass = self.lg.add_class(self.center_id)
        self.g['id'] = addClass['id']  #将班级 ID 全局，方便调用删除
        self.assertTrue('id' in addClass)

