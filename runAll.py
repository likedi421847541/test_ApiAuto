# -*- coding:utf-8 -*-
import os
import unittest
import time
from common import  HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common import demo
import smtplib
import json
import yaml
cur_path = os.path.dirname(os.path.realpath(__file__)) # 当前脚本所在文件的真实路径
print(cur_path)
def login():
    url = 'http://api2.learning-genie-api.com/api/v1/account/login'
    data = {"email": "421847541@qq.com", "password": "12345678q", "from": "web", "emailLoginExpireFlag": ""}
    data = json.dumps(data)
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;   WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    login = demo.RunMain().run_main('post', url, data=data, headers=headers)
    login = json.loads(login)
    print(login['token'],login['user_id'])
    token = login['token']
    user_id = login['user_id']
    return token,user_id

def write_yaml(value1,value2):
    '''
    把获取到的 token值写入到 yaml 文件
    :param value:
    :return:
    '''
    ypath = os.path.join(cur_path,'common','token.yaml')
    print(ypath)
    # 需写入的内容
    t = {'token':value1,'user_id':value2}
    # 写入到 yaml 文件
    with open(ypath,'w',encoding='utf-8') as  f:
        yaml.dump(t,f)
def add_case(caseName='case',rule="test_*.py"): # 第一步：加载所有的测试用例
    '''caseName='case',表示存放用例的wenjianming
       rule='test.py'，表示匹配用例脚本名称的规则，默认匹配test开头的所有用例'''
    case_path = os.path.join(cur_path,caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:{}".format(case_path))
    #定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover
def run_case(all_case,reportName='report'):
    '''第二步：执行所有的用例，并将结果写入 HTML 测试报告
        把第一步加载到用例的参数传入这个参数，测试报告的文件名称默认 report文件夹

    '''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    print('report path:{}'.format(report_abspath))
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告，测试结果如下：',
                                           description=u'用例执行情况')
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    list = os.listdir(report_path)
    list.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u'最新测试生成的报告：'+list[-1])
    report_file = os.path.join(report_path,list[-1])
    return report_file
def send_email(sender,psw,receiver,smtpserver,report_file,port):
    '''
    第四步：发送最新的测试报告内容
    '''
    with open(report_file,'rb') as f:
        mail_body=f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject'] = u'自动化测试报告'
    msg['from']= sender
    msg['to']=psw
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition']='attachment;filename="report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')
if __name__ == '__main__':
    a = login()
    token = a[0]
    user_id = a[1]
    print('token 的类型是：',type(token))
    write_yaml(token,user_id)
    all_case = add_case() # 第一步：加载用例
    # 生成测试报告的路径
    run_case(all_case) # 第二步：执行用例
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path,'report')#用例文件夹
    report_file = get_report_file(report_path) # 获取最新的测试报告
    # 邮箱配置
    from testFile import readConfig
    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    send_email(sender,psw,receiver,smtp_server,report_file,port)
    login()