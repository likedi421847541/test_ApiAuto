# -*- coding:utf-8 -*-
import unittest
import json
from common import demo
from common.read_token import  get_token
from common.read_token import  get_userid
class AddCenters_001(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        cls.user_id = get_userid()
    def test_addcenters(self):
        url = 'http://api2.learning-genie-api.com/api/v1/centers'
        data = {"name":"e","user_id":self.user_id,"send_report_time":"18:00:00","timezone":"Asia/Shanghai"}
        data = json.dumps(data)
        headers = {'Content-Type':'application/json;charset=UTF-8',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Token':self.token,
                   'X-UID':self.user_id}
        login = demo.RunMain().run_main('post',url,data=data,headers=headers)

        print(login)
    if __name__ == '__main__':
        test_addcenters()