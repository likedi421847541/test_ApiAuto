# -*- coding:utf-8 -*-
import requests
import json
import datetime
import random
import string
from common.read_token import get_token
from common.read_token import get_userid
from runAll import write_yaml


class LG():
    # 随机获取四位数字和字母的字符串
    def __init__(self):
        self.s = requests.session()
        self.url = 'http://api2.learning-genie-api.com/api/v1'
        self.current_year = datetime.datetime.now().year
        self.next_year = int(datetime.datetime.now().year) + 1
        self.current_time = str(datetime.datetime.now())[:-3]

    def login(self, email1='421847541@qq.com', password='12345678q'):
        url = self.url + '/account/login'
        data = {"email": email1, "password": password, "from": "web", "emailLoginExpireFlag": ""}
        data = json.dumps(data)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        login = self.s.request('post', url, data=data, headers=headers).json()
        if 'email' in login:
            token = login['token']
            user_id = login['user_id']
            write_yaml(token, user_id)
        # print(type(login))
        # print(login)
        # print(login['token'],login['user_id'],login['email'])
        return login

    def get_headers(self):
        token = get_token()
        user_id = get_userid()
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                   'X-LG-Platform': 'web',
                   'X-LG-TimezoneOffset': '8',
                   'Connection': 'keep_alive',
                   'X-LG-Token': token,
                   'X-UID': user_id}
        return headers


    def add_center(self, center_name):
        url = self.url + '/centers'
        data = {"name": center_name, "user_id": get_userid(), "send_report_time": "18:00:00",
                "timezone": "Asia/Shanghai"}
        data = json.dumps(data)
        headers = self.get_headers()

        centers = self.s.request('post', url, data=data, headers=headers).json()
        return centers


    def edit_centers(self, center_id, CenterName):
        url = self.url + '/centers/' + center_id
        data = {"id": center_id, "name": CenterName, "timezone": "Asia/Shanghai",
                "send_report_time": "20:00:00", "logo_media_id": None,
                "logo_url": "https://d2urtjxi3o4r5s.cloudfront.net/images/center_logo.png",
                "user_id": get_userid()}
        data = json.dumps(data)
        headers = self.get_headers()
        try:
            edit_centers = self.s.put(url, data, headers=headers)
            return edit_centers
        except KeyError:
            print(edit_centers['msg'])
    def delete_centers(self, center_id):
        url = self.url + '/centers/' + center_id
        headers = self.get_headers()
        del_centers = self.s.delete(url, headers=headers)

    def delete_centers_errmsg(self, center_id):
        url = self.url + '/centers/' + center_id
        headers = self.get_headers()
        del_centers = self.s.delete(url, headers=headers).json()
        return del_centers

    def get_centers(self):
        url = self.url + '/users/' + get_userid() + '/getCenterGroupByUserId?agencyId='
        headers = self.get_headers()
        centers = self.s.get(url, headers=headers).json()
        return centers

    def get_stageId(self):  # 获取班级年龄段
        url = self.url + '/groups/stages'
        headers = self.get_headers()
        stage_id = self.s.get(url, headers=headers).json()
        # print(stage_id[0])
        return stage_id

    def get_goals(self):
        url = self.url + '/goals'
        headers = self.get_headers()
        goals = self.s.get(url, headers=headers)
        return goals

    def add_class(self, center_id, class_name, portfolio_id='', period_id=''):
        url = self.url + '/groups'
        headers = self.get_headers()
        stage_id = self.get_stageId()[0]['id']
        data = {
            "stage_id": stage_id,
            "portfolio_id": portfolio_id,
            "childPortfolio_id": portfolio_id,
            "icon_url": 0,
            "name": class_name,
            "classPortfolioId": "",
            "programPortfolioId": "",
            "center_id": center_id,
            "periodGroupId": period_id
        }
        data = json.dumps(data)
        class_LG = self.s.post(url, data, headers=headers).json()
        return class_LG

    def del_class(self, group_id):
        if group_id != '':
            url = self.url + '/groups/' + group_id
            headers = self.get_headers()
            del_groups = self.s.delete(url, headers=headers)
        else:
            pass

    def add_child(self, groupid):  # 添加小孩
        url = self.url + '/students'
        headers = self.get_headers()
        data = {
            "birthDate": "04/01/2018",
            "enrollmentDate": "2019-04-01",
            "firstName": "test",
            "gender": "MALE",
            "groupId": groupid,
            "lastName": '001',
            "withdrawnDate": "",
            "checkEnrollmentDate": True,
            "update": False,
            "attrs": [],
            "currentTime": self.current_time,
            "periods": []
        }
        data = json.dumps(data)
        child = self.s.post(url, data=data, headers=headers).json()
        # print(child)
        return child

    def inactive_child(self, child_id):
        url = self.url + '/students/inactive/' + child_id
        headers = self.get_headers()
        #print(url)
        self.s.post(url, headers=headers)

    def merge_child(self,child_id,group_id):
        url = self.url+'/students/'+child_id+'?web=1'
        print(url)
        data = {
            "birthDate": "07/30/2018",
            "enrollmentDate": "2018-08-05",
            "firstName": "0",
            "gender": "MALE",
            "groupId": group_id,
            "lastName": "11111",
            "privatePhoto": False,
            "middleName": None,
            "withdrawnDate": "",
            "avatarMediaId": None,
            "email": None,
            "phoneNumber": None,
            "agencyId": "",
            "update": False,
        }
        data = json.dumps(data)
        headers = self.get_headers()
        result = self.s.put(url,data=data,headers = headers)
        print(result)
    def del_child(self, child_id):
        url = self.url + '/students/' + child_id
        self.s.delete(url, headers=self.get_headers())

    def get_group_student(self, group_id):  # 获取指定班级下的小孩
        url = self.url + '/students'
        param = {'groupId': group_id,
                 'order': 'asc',
                 'pageNum': '1',
                 'pageSize': '1000',
                 'search':'',
                 'sort':'lastName'
                 }
        student = self.s.get(url, params=param, headers=self.get_headers()).json()
        return student
    def search_student(self, name):  # 按小孩名搜索学生
        url = self.url + '/students'
        param = {
            'order': 'asc',
            'pageNum': '1',
            'pageSize': '50',
            'search': name,
            'sort': 'lastName'
        }
        students = self.s.get(url, params =param, headers=self.get_headers()).json()
        return students

if __name__ == '__main__':
    s = requests.session()
    LG().login()
    LG().add_center('abc')
    LG().get_goals()
