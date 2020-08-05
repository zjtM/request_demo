import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import os
import time 

import sys
sys.path.append('..')

import getcwd
from Logs.log import log1
from Common.Base_test import webRequests

rq = time.strftime('%y%m%d', time.localtime(time.time())) #获取本地时间 转换成日期
my_mail = webRequests()
sender = my_mail.config_get('sender','email')
password = my_mail.config_get('sender', 'password')
username = my_mail.config_get('sender','username')
users = my_mail.config_options('addressed')
addressed_email = my_mail.config_addkey(users)

path = getcwd.get_cwd()
file = os.path.join(path, 'report/测试报告.html') #测试报告地址

def mail():
    try:
        #带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(['发件人姓名',sender]) #括号里对应发件人邮箱昵称、邮箱号
        log1.info('发件人邮箱：%s' %sender)
        message['To'] = formataddr(['收件人', addressed_email])
        log1.log('收件人邮箱：%s' %addressed_email)
        message['Subject'] = rq + '测试报告' #邮件主题（标题）

        #邮件正文
        message.attach(MIMEMultipart('附件为测试报告', 'plain', 'utf-8'))

        #构造附件
        att1 = MIMEText(open(file,'rb').read(), 'base64', 'uft-8')
        log1.info('读取附件')
        att1['Content-Type'] = 'application/octet-stream'
        #filename附件名称， 当名称为中文时
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att1)
        log1.info('添加附件')

        server = smtplib.SMTP_SSL('smtp.qq.com', 465) # 发件人邮箱中SMTP服务器，一般端口是25
        log1.info('连接QQ邮箱SMTP服务')
        server.login(sender,password) #登录发件人邮箱
        log1.info('连接成功')
        server.sendmail(sender,addressed_email,message.as_string())#发件人、收件人、发送邮件
        server.quit() #退出登录
        log1.info('邮件发送成功')
    except Exception:
        log1.log('发送失败', exc_info=1)