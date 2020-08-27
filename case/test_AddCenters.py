# -*- coding:utf-8 -*-
import unittest
from common.LG import LG
import requests
import  string
import  random
class AddCenters_001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.lg = LG()
    def setUp(self):
        self.g  = globals()
    def tearDown(self):
        t = self.g["id"]
        self.lg.delete_centers(t)
    def test_addcenters(self):
        center_name = ''.join(random.sample(string.ascii_letters + string.digits,
                                            4))  # 随机生成字符串， random.sample(str,num)从 str 字符串中随机选取 num 个字符
        #print(center_name)
        self.lg.login()
        centers = self.lg.add_center(center_name)
        self.assertTrue('id'in centers)
        center_id = centers['id']
        self.g["id"] = center_id
