#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib.request
#from bs4 import BeautifulSoup
import re
response=urllib.request.urlopen('http://2017.ip138.com/ic.asp')
html=response.read().decode('gb2312')
#soup = BeautifulSoup(html,"lxml")
reg =r"\d+.\d+.\d+.\d+"
iplist = re.findall(reg,html)
for ip in  iplist:
    print (ip)