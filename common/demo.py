# -*- coding:utf-8 -*-
import requests
import json
class RunMain():   # 封装 get/post 方法
    def send_post(self,url,data,headers):
        result = requests.post(url = url,data = data,headers= headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res
    def send_get(self,url,data,headers):
        result = requests.get(url = url,data = data,headers = headers).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def send_delete(self,url,headers):
        result = requests.request()
    def run_main(self,method,url=None,data=None,headers = None):
        result = None
        if method  == 'get':
            result = self.send_get(url,data,headers)
        elif method == 'post':
            result = self.send_post(url,data,headers)
        return result
if __name__ == '__main__':
    url = 'http://127.0.0.1:8888/login'
    data1 = {'name':'xiaoming','pwd':'111'}
    data2 = 'name=xiaoming&pwd=11'
    result1 = RunMain().run_main('post',url,data1)
    result2 = RunMain().run_main('get',url,data2)
    print(result1)
    print(result2)