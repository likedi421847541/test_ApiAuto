# -*- coding:utf-8 -*-
import unittest
from common.LG import LG
import requests
class AddCenters_001(unittest.TestCase):
    lg =LG()
    lg.login()
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.g = globals()
    # # 随机生成字符串， random.sample(str,num)从 str 字符串中随机选取 num 个字符
    def tearDown(self):
        self.lg.delete_centers(self.g['01'])
    def test_addcenters(self):
        '''
        用例一：正常添加学校
        :return:
        '''
        centers = self.lg.add_center()
        self.g['01'] = centers['id']
        self.assertTrue('id'in centers)
        #self.lg.delete_centers(g)
    def test_addcenters_rename(self):
        """
        用例二：添加重复学校名字
        :return:
        """
        center_name = 'chongfu_center001'
        centers = self.lg.add_center(center_name)
        self.g['01'] = centers['id']
        centers_01 = self.lg.add_center(center_name)
        self.assertIn(centers_01['error_code'],'centername_exist')
        #self.lg.delete_centers(g)
    def test_editcenters_name(self):
        '''
        用例三：编辑学校
        :return:
        '''
        self.centers = self.lg.add_center()
        self.g['01'] = self.centers['id']
        editCenterName = 'EditCenter'
        centers_edit = self.lg.edit_centers(center_id = self.centers['id'],CenterName=editCenterName)
        centers = self.lg.get_centers()
        self.a = []
        for i in centers:
            for values in i:
                self.a.append(i[values])
        self.assertIn(editCenterName, self.a)
        #self.lg.delete_centers(self.centers['id'])
    def test_del_centers(self):
        centers = self.lg.add_center()
        centers_id_yuqi = centers['id']
        self.lg.delete_centers(centers_id_yuqi)
        centers = self.lg.get_centers()
        #print(type(centers))
        self.a=[]
        for i in centers:
            for values in i:
                self.a.append(i[values])
        #print(self.a)
        self.assertNotIn(centers_id_yuqi,self.a)
