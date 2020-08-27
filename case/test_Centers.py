# -*- coding:utf-8 -*-
import unittest
from common.LG import LG
import requests
import  string
import  random
import json
class AddCenters_001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.lg = LG()

    def setUp(self):
        self.g  = globals()
        self.center_name = ''.join(random.sample(string.ascii_letters + string.digits,
                                                4))  # 随机生成字符串， random.sample(str,num)从 str 字符串中随机选取 num 个字符
    # def tearDown(self):
    #     t = self.g["id"]
    #     self.lg.delete_centers(t)
    def test_addcenters(self):
        '''
        用例一：正常添加学校
        :return:
        '''
        self.lg.login()
        centers = self.lg.add_center(self.center_name)
        g = centers['id']
        self.assertTrue('id'in centers)
        self.lg.delete_centers(g)
    def test_addcenters_rename(self):
        """
        用例二：添加重复学校名字
        :return:
        """
        center_name = 'chongfu_center001'
        self.lg.login()
        centers = self.lg.add_center(center_name)
        g = centers['id']
        centers_01 = self.lg.add_center(center_name)
        self.assertIn(centers_01['error_code'],'centername_exist')
        self.lg.delete_centers(g)
    def test_editcenters(self):
        '''
        用例三：编辑学校
        :return:
        '''
        self.lg.login()
        self.centers = self.lg.add_center(self.center_name)
        self.center_id = self.centers['id']
        data = {"id":self.center_id,"name":"edit_center","timezone":"Asia/Shanghai","send_report_time":"20:00:00","logo_media_id":None,"logo_url":"https://d2urtjxi3o4r5s.cloudfront.net/images/center_logo.png","user_id":"10CACAAF-B403-4EE8-AB74-2F20D97D8C7D"}
        data = json.dumps(data)
        centers = self.lg.edit_centers(center_id = self.center_id,data=data)
        centers = self.lg.get_centers()
        self.a = []
        for i in centers:
            for values in i:
                self.a.append(i[values])
        self.assertIn('edit_center', self.a)
        self.lg.delete_centers(self.centers['id'])
    def test_del_centers(self):
        self.lg.login()
        centers = self.lg.add_center(self.center_name)
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
