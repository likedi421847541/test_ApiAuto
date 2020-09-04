import datetime
import requests
import json
from common import LG
# -*- coding:utf-8 -*-

class Period():
    lg = LG.LG()
    lg.login()
    def __init__(self):
        #self.headers = self.lg.get_headers()
        self.s = requests.session()
        self.url = 'http://api2.learning-genie-api.com/api/v1'
        self.current_year = datetime.datetime.now().year
        self.next_year = int(datetime.datetime.now().year) + 1
    def add_period(self, period_name):  # 添加 season 类型的周期
        url = self.url + '/periods/setGroups'
        data = {"name": period_name,
                "orderNum": 1,
                "schoolYear": "{}-{}".format(self.current_year,self.next_year),
                "firstAssessmentDuration": "60",
                "type": "Season",
                "policy": "CUT_OFF_DATE",
                "periods": [{
                    "alias": "Fall {}".format(self.current_year),
                    "fromAtLocalString": "08/30/{}".format(self.current_year),
                    "toAtLocalString": "10/28/{}".format(self.current_year),
                    "cutOffDayString": "10/18/{}".format(self.current_year)},
                    {
                        "alias": "Winter {}".format(self.current_year),
                        "fromAtLocalString": "10/29/{}".format(self.current_year),
                        "toAtLocalString": "01/12/{}".format(self.current_year),
                        "cutOffDayString": "12/17/{}".format(self.current_year)},
                    {
                        "alias": "Spring {}".format(self.next_year),
                        "fromAtLocalString": "01/13/{}".format(self.next_year),
                        "toAtLocalString": "04/15/{}".format(self.next_year),
                        "cutOffDayString": "02/15/{}".format(self.next_year)}],
                "centers": [],
                "shortPeriodDays": "60",
                "latePolicys": [{"metaKey": "CUT_OFF_DATE_TYPE", "metaValue": "ENROLLMENT CUT DATE"}],
                "settedMix": True}
        headers = self.lg.get_headers()
        data = json.dumps(data)
        period = self.s.post(url,data,headers = headers).json()
        return period
    def del_period(self,period_id):
        url = self.url +'/periods/deleteGroup'
        data = {'periodGroupId':period_id}
        print(url)
        headers = self.lg.get_headers()
        #self.s.options(url,params = data,headers = headers)
        result = self.s.get(url,params = data,headers = headers).json()
        return result
if __name__ == '__main__':
    lg = LG.LG()
    lg.login()
    pe = Period()
    pe.add_period('test_1650')
