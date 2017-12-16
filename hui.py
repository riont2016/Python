#!/usr/bin/env
#-*- coding:utf-8 -*-
"""
从中国银行提取实时汇率到本地数据库
"""
__author__="riont"
import re
from lxml import etree
import requests
import pymysql
HOST = '127.0.0.1'
DB = "money"
USER = 'root'
PSWD = 'yall123'
country =["英镑","港币","美元","瑞士法郎","新加坡元","瑞典克朗","丹麦克朗","挪威克朗","日元","加拿大元","澳大利亚元","欧元","澳门元","菲律宾比索","泰国铢","新西兰元","韩国元","卢布","林吉特","新台币","印尼卢比","巴西里亚尔","阿联酋迪拉姆","印度卢比","南非兰特","沙特里亚尔","土耳其里拉"]
url = 'http://www.boc.cn/sourcedb/whpj/index.html'
html = requests.get(url).content.decode('utf8')
for str_country in country:
    a = html.index("<td>"+ str_country + "</td>")
    s = html[a:a + 300]
    result = re.findall('<td>(.*?)</td>', s)
    conn = pymysql.connect(host=HOST, user=USER,passwd=PSWD,charset="utf8")
    cursor = conn.cursor()
    conn.select_db(DB)
    name = result[0]
    buyPrice1 = result[1]
    buyPrice2 = result[2]
    sellPrice1 = result[3]
    sellPrice2 = result[4]
    midPrice = result[5]
    publishyear = result[6]
    publishtime = result[7]
    gettime = publishyear + ' ' + publishtime
    sql_content = "replace into exchange_rate(name,buyPrice1,buyPrice2,sellPrice1,sellPrice2,midPrice,gettime) values ('%s','%s','%s','%s','%s','%s','%s')" %(name,buyPrice1,buyPrice2,sellPrice1,sellPrice2,midPrice,gettime)
    cursor.execute(sql_content)
    conn.commit()   
 #   with open('汇率.txt', 'a+') as f:
 #       f.write(result[0] + '\n')
  #      f.write('现汇买入价：' + result[1] + '\n')
   #     f.write('现钞买入价：' + result[2] + '\n')
    #    f.write('现汇卖出价：' + result[3] + '\n')
    #    f.write('现钞卖出价：' + result[4] + '\n')
    #    f.write('中行折算价：' + result[5] + '\n')
    #    f.write('发布时间：' + result[6] + ' ' + result[7] + '\n')
    #    f.write('\n')
