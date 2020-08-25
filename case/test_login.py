3# -*- coding:utf-8 -*-
import unittest
import json
from common import demo
class Login_001(unittest.TestCase):
    def test_login(self):
        url = 'http://api2.learning-genie-api.com/api/v1/account/login'
        data = {"email":"421847541@qq.com","password":"12345678q","from":"web","emailLoginExpireFlag":""}
        data = json.dumps(data)
        headers = {'Content-Type':'application/json;charset=UTF-8',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        login = demo.RunMain().run_main('post',url,data=data,headers=headers)
        self.assertTrue(login)
        print(login)
    if __name__ == '__main__':
            test_login()
