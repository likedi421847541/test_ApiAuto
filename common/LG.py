# -*- coding:utf-8 -*-
import requests
import json
import random
import string
from common.read_token import  get_token
from common.read_token import  get_userid
from runAll import write_yaml
class LG():
    name = ''.join(random.sample(string.ascii_letters + string.digits, 4)) # 随机获取四位数字和字母的字符串

    def __init__(self):
        self.s = requests.session()
        self.url = 'http://api2.learning-genie-api.com/api/v1'
    def login(self,email1='421847541@qq.com',password='12345678q'):
        url = self.url +'/account/login'
        data = {"email": email1, "password": password, "from": "web", "emailLoginExpireFlag": ""}
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        login = self.s.request('post', url, data=data, headers=headers).json()
        if 'email' in login:
            token = login['token']
            user_id = login['user_id']
            write_yaml(token, user_id)
            self.token = get_token()
            self.user_id = get_userid()
        # print(type(login))
        # print(login)
        # print(login['token'],login['user_id'],login['email'])
        return login
    def get_headers(self):
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Token': self.token,
                   'X-UID': self.user_id}
        return headers

    def add_center(self,center_name = name):
        url = self.url+'/centers'
        data = {"name": center_name, "user_id": self.user_id, "send_report_time": "18:00:00",
                "timezone": "Asia/Shanghai"}
        headers = self.get_headers()
        data = json.dumps(data)
        centers = self.s.request('post', url, data=data, headers=headers).json()
        return centers
    def edit_centers(self,center_id,CenterName):
        url = self.url+'/centers/' + center_id
        data = {"id": center_id, "name": CenterName, "timezone": "Asia/Shanghai",
                "send_report_time": "20:00:00", "logo_media_id": None,
                "logo_url": "https://d2urtjxi3o4r5s.cloudfront.net/images/center_logo.png",
                "user_id": self.user_id}
        data = json.dumps(data)
        headers = self.get_headers()
        edit_centers = self.s.put(url,data,headers = headers)
        return edit_centers
    def delete_centers(self,center_id):
        url = self.url+'/centers/'+center_id
        headers = self.get_headers()
        del_centers = self.s.delete(url,headers = headers)
    def get_centers(self):
        url = self.url+'/users/'+self.user_id+'/getCenterGroupByUserId?agencyId='
        headers = self.get_headers()
        centers = self.s.get(url,headers = headers).json()
        return centers
    def get_stageId(self): #获取班级年龄段
        url = self.url+'/groups/stages'
        headers = self.get_headers()
        stage_id = self.s.get(url,headers=headers).json()
        print(stage_id[0])
        return stage_id
    def add_class(self,center_id,class_name = name):
        url = self.url+'/groups'
        headers = self.get_headers()
        stage_id = self.get_stageId()[0]['id']
        data = {"center_id":center_id , "programPortfolio_id": "",
         "stage_id": stage_id, "icon_url": 0, "name": class_name, "classPortfolioId": "",
         "programPortfolioId": ""}
        data = json.dumps(data)
        class_LG = self.s.post(url,data,headers = headers) .json()
        return class_LG
    def del_class(self,group_id):
        url = self.url + '/groups/' + group_id
        headers = self.get_headers()
        del_groups = self.s.delete(url, headers=headers)
if __name__ == '__main__':
    s = requests.session()
    login = LG().login()
    LG().get_headers()
    LG().add_center('abc')
