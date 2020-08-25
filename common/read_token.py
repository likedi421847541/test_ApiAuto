# -*- coding:utf-8 -*-
import yaml
import os
cur = os.path.dirname(os.path.realpath(__file__))
def get_token(yamlName='token.yaml'):
    '''
    从 token.yaml 读取 token 值
    :param yamlName:
    :return:
    '''
    p = os.path.join(cur,yamlName)
    f = open(p,encoding = 'utf-8')
    a = f.read()
    t = yaml.load(a,Loader = yaml.FullLoader)
    f.close()
    t= t["token"]
    print (t)
    return t

def get_userid(yamlName='token.yaml'):
    p = os.path.join(cur, yamlName)
    f = open(p, encoding='utf-8')
    a = f.read()
    t = yaml.load(a, Loader=yaml.FullLoader)
    f.close()
    return t['user_id']

if __name__ == '__main__':
    print(get_token())