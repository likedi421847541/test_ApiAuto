# -*- coding:utf-8 -*-
import unittest
import json
import random
from common import demo
from common.read_token import  get_token
from common.read_token import  get_userid
from common.LG import LG
import requests
from runAll import write_yaml
class AddCenters_001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        s = requests.session()
        cls.lg = LG(s)
        token = LG(s).login()[1]
        user_id = LG(s).login()[2]
        write_yaml(token, user_id)
        cls.token = get_token()
        cls.user_id = get_userid()
    def setUp(self):
        self.g = globals()
    def test_addcenters(self):
        center_name = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
        centers = self.lg.add_center(center_name,self.token,self.user_id)
        center_id = centers['id']
        assert

    # def tearDown(self):
    #     url = 'http://api2.learning-genie-api.com/api/v1/centers/'+self.g['id']
    #     #print (url)
    #     headers = {'Content-Type': 'application/json;charset=UTF-8',
    #                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    #                'X-LG-Token': self.token,
    #                'X-UID': self.user_id}
    #     del_centers = requests.delete(url,headers = headers)
    if __name__ == '__main__':
        test_addcenters()