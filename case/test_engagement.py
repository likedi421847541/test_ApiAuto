# -*- coding:utf-8 -*-
import unittest
from common.LG import LG
class TestEngagement(unittest.TestCase):
    lg = LG()
    lg.login()
    g = globals()  # 全局变量
    g['id'] = ''  # 先定义为空
    c_id = lg.add_center('testEnagement')['id']  # 添加学校
    g_id = lg.add_class(c_id, 'forchild')['id'] #添加班级
    s_id = lg.add_child(g_id)['id'] #添加小孩
    filepath = r'C:\Users\Administrator\Desktop\test.jpg'
    @classmethod
    def setUpClass(cls):
        cls.mediaId = cls.lg.uploadFile('jpg',cls.filepath)['id']
        #print(cls.mediaId)
    @classmethod
    def tearDownClass(cls):
        cls.lg.del_child(cls.s_id)
        cls.lg.del_class(cls.g_id)
        cls.lg.delete_centers(cls.c_id)
    def test_addActivity_photo(self):
        result = self.lg.add_activity(childId=self.s_id,meidiaId=self.mediaId)  #
        print(result)