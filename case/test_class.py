# -*- coding:utf-8 -*-
import unittest
import requests
import string
import random
import json
from common.LG import LG
from common.Period import Period
class LGClass(unittest.TestCase):
    g = globals() # 全局变量   globals()函数只能有一个，如果定义多个，可以以字典的 key 值进行传递
    #p_id = globals() # 周期id
    g['id'] = '' # 默认为空
    g['pid'] = ''
    lg = LG()
    pe = Period()
    lg.login()  # 先登录获取 token 和 user_id
    center_id = lg.add_center('ForClass')['id']  # 添加学校，获取学校 ID
    @classmethod
    def setUpClass(cls):
        cls.IT_id = 'E163164F-BDCE-E411-AF66-02C72B94B99B'
        cls.s = requests.session()

    def setUp(self):
        self.name = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    def tearDown(self):
        self.lg.del_class(self.g['id'])
        # del_p = self.pe.del_period(self.p_id['id'])
        # print(del_p)
    @classmethod
    def tearDownClass(cls):
        cls.pe.del_period(cls.g['pid'])
        cls.lg.delete_centers(cls.center_id)
    def test_add_class(self):
        addClass = self.lg.add_class(self.center_id,self.name)
        self.g['id'] = addClass['id']  #将班级 ID 全局，方便调用删除
        self.assertTrue('id' in addClass)
    def test_add_PeSeClass(self): # 添加带有 season 周期的班级
        period = self.pe.add_period(self.name)['periodGroupId']
        self.g['pid'] = period
        addClass = self.lg.add_class(self.center_id,self.name,portfolio_id=self.IT_id,period_id=period)
        self.g['id'] = addClass['id']
        self.assertTrue('id'in addClass)
        #self.pe.del_period(period)  # 删除周期添加的测试数据
    def test_emptyC_class(self): # 空学校 id
        addClass = self.lg.add_class(center_id='',class_name=self.name)
        err_message = 'CenterId is required.'
        self.assertEqual(addClass['message'],err_message)
    def test_empty_class(self):#添加空名字的班级
        addClass = self.lg.add_class(center_id=self.center_id,class_name='')
        err_message = 'Group name is required.'
        self.assertEqual(addClass['message'],err_message)
    def test_chongfu_class(self): # 添加重复班级
        addClass = self.lg.add_class(self.center_id,'chongfu_class')
        self.g['id'] = addClass['id']
        addClass = self.lg.add_class(self.center_id, 'chongfu_class')
        err_message = 'The class name already exists.'
        self.assertEqual(addClass['message'],err_message)
    def test_del_class(self):#删除班级
        addClass = self.lg.add_class(self.center_id,class_name=self.name)  # 添加班级
        #group = self.lg.get_class(self.center_id)['groups']  # 获取指定学校下的班级，返回一个列表
        addClass['id'] = str.upper(addClass['id'])    # get_class 返回的是小写，经 str.upper 转换为大写
        self.lg.del_class(addClass['id']) #删除班级
        group = self.lg.get_class(self.center_id)['groups']  # 获取指定班级下的班级信息
        print(group)
        a = []
        for items in group:
            for keys in items:
                a.append(items[keys])
        self.assertTrue(addClass['id'] not in  a)
    def test_del_haveStuClass(self):
        addClass = self.lg.add_class(self.center_id,class_name=self.name)  # 添加班级
        self.g['id'] = addClass['id']
        print(addClass)
        addClass['id'] = str.upper(addClass['id'])
        addCild = self.lg.add_child(addClass['id'])  # 添加小孩
        print(addCild)
        err_msg = self.lg.del_class(addClass['id']).json()['error_message']  # 删除班级
        print(err_msg)
        msg = 'The group has users or children.'
        self.assertEqual(msg,err_msg)
        self.lg.del_child(addCild['id'])




