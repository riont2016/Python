#!/usr/bin/env python3  
#coding: utf-8
“”“
利用163smtp发送邮件，SSL方式
”“”
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header
sender = '******' #这里填写发送者的邮箱  
receiver = '*****' #这里填写接收者的邮箱  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '********' #smtp用户名，邮箱用户名
password = '********'  #smtp密码，邮箱密码
msg = MIMEText('你好','text','utf-8') 
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP_SSL('smtp.163.com',465)
smtp.set_debuglevel(1) #这里启用调试模式
smtp.docmd("HELO server")
smtp.ehlo()
#smtp.starttls()
smtp.ehlo()  
smtp.set_debuglevel(1)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  
