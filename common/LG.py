# -*- coding:utf-8 -*-
import requests
import json
class LG():
    def __init__(self,s):
        self.s = s
    def login(self,email='421847541@qq.com',password='12345678q'):
        url = 'http://api2.learning-genie-api.com/api/v1/account/login'
        data = {"email": email, "password": password, "from": "web", "emailLoginExpireFlag": ""}
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        login = self.s.request('post', url, data=data, headers=headers).json()
        # print(type(login))
        # print(login)
        # print(login['token'],login['user_id'],login['email'])
        return login['email'],login['token'],login['user_id']

    def add_center(self,center_name,token,user_id):
        url = 'http://api2.learning-genie-api.com/api/v1/centers'
        data = {"name": center_name, "user_id": user_id, "send_report_time": "18:00:00",
                "timezone": "Asia/Shanghai"}
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Token': token,
                   'X-UID': user_id}
        centers = self.s.request('post', url, data=data, headers=headers).json()
        print(centers)
if __name__ == '__main__':
    s = requests.session()
    login = LG(s).login("421847541@qq.com","12345678q")
    LG(s).add_center('abc',login[1],login[2])
