# -*- coding:utf-8 -*-
import requests
import json
import string
import random
import yaml
from common.read_token import  get_token
from common.read_token import  get_userid
from runAll import write_yaml
class LG():
    def __init__(self):
        self.s = requests.session()
    def login(self,email='421847541@qq.com',password='12345678q'):
        url = 'http://api2.learning-genie-api.com/api/v1/account/login'
        data = {"email": email, "password": password, "from": "web", "emailLoginExpireFlag": ""}
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        login = self.s.request('post', url, data=data, headers=headers).json()
        token = login['token']
        user_id = login['user_id']
        write_yaml(token, user_id)
        self.token = get_token()
        self.user_id = get_userid()
        # print(type(login))
        # print(login)
        # print(login['token'],login['user_id'],login['email'])
        return login,login['email']

    def add_center(self,center_name):

        url = 'http://api2.learning-genie-api.com/api/v1/centers'
        data = {"name": center_name, "user_id": self.user_id, "send_report_time": "18:00:00",
                "timezone": "Asia/Shanghai"}
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Token': self.token,
                   'X-UID': self.user_id}
        data = json.dumps(data)
        centers = self.s.request('post', url, data=data, headers=headers).json()
        return centers
    def delete_centers(self,center_id):
        url = 'http://api2.learning-genie-api.com/api/v1/centers/'+center_id
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Token': self.token,
                   'X-UID': self.user_id}
        del_centers = self.s.delete(url,headers = headers)
if __name__ == '__main__':
    s = requests.session()
    login = LG(s).login("421847541@qq.com","12345678q")
    LG(s).add_center('abc',login[1],login[2])
