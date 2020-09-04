# -*- coding:utf-8 -*-
import unittest
import requests
import string
from common.LG import  LG
from common.Period import Period
class Period(unittest.TestCase):
    lg = LG()
    pe = Period()
    lg = lg.login()
    period = globals()
    def tearDown(self):
        self.pe.del_period(self.period['id'])
    def test_add_Period(self):
        pe = self.pe.add_period('test_1354')['periodGroupId']
        self.period['id'] = pe
