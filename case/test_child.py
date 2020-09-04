# -*- coding:utf-8 -*-
import unittest
import datetime
import requests
from common.LG import LG


class Child(unittest.TestCase):
    lg = LG()
    lg.login()
    g = globals() # 全局变量
    g['id'] = '' # 先定义为空
    c_id = lg.add_center('forchild')['id']
    g_id = lg.add_class(c_id, 'forchild')['id']
    def setUp(self):
        self.child = self.lg.add_child(self.g_id)
    def tearDown(self):
        self.lg.del_child(self.g['id'])
    @classmethod
    def tearDownClass(cls): # 后置条件
        cls.lg.del_class(cls.g_id)  # 删除添加的班级
        cls.lg.delete_centers(cls.c_id) # 删除添加的学校
    def test_add(self):  # 添加小孩

        self.g['id'] = self.child['id']
        #print(child)
        self.assertTrue('id' in self.child)

    def test_inacitive(self):  # 小孩离校
        #child_id = self.lg.add_child(self.g_id, 'lixiao')['id']  # 先添加小孩
        self.g['id'] = self.child['id']
        self.lg.inactive_child(self.child['id'])
        # 下面是断言，判断班级下没有该小孩
        student = self.lg.get_group_student(self.g_id)  # 获取该班级下的小孩
        print(student)
        self.assertTrue(self.child['id'] not in student)

    def test_del(self):  # 删除小孩
        #child_id = self.lg.add_child(self.g_id, 'del')['id']  # 先添加小孩
        self.lg.del_child(self.child['id'])  # 删除小孩
        # 断言
        result = self.lg.search_student('del')
        #print(result)
        self.assertEqual(result['total'],0)

    def test_edit_merge(self):
        group_id = self.lg.add_class(self.c_id,'for_merge')['id']  # 先添加要转移到的班级
        self.lg.merge_child(self.child['id'],group_id)
        # 断言
        student = self.lg.get_group_student(group_id) # 获取转移后班级的小孩
        x = student['results']   #  获取字典中的字典 key 值为 results，返回一个列表
        x = x[0]  # 获取列表中的 字典
        x = x['id']  # 获取字典中的 key值 id
        print(x)

        # c = []
        # for items in student['results']:
        #     for i in items:
        #         c.append(items[i])
        #     print(c)
        #self.assertTrue(self.child['id'] in c)
        self.assertTrue(self.child['id'] in x)
        self.lg.del_child(self.child['id']) # 删除小孩
        self.lg.del_class(group_id)  # 删除刚添加的转移到的班级


