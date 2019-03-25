'''
#发短信
#C43392168
#2bb05d15e94a5ad278c0fc6bb49d0940

# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C43392168"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "2bb05d15e94a5ad278c0fc6bb49d0940"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "15279699889"
    text = "您的验证码是：1234。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))
'''
'''
#发邮件
#导入发送邮件的库
import smtplib
#邮件文本的库
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = 'smtp.163.com'
#发邮件的地址
Sender = '15279699889@163.com'
#发送者邮箱的密码(不是登陆密码，是客户端授权密码)
password = 'z960320'

#设置发送的内容
message = 'Hailong now is learning Python' #字符串格式
msg = MIMEText(message)            #转换成邮件文本的格式
#设置主题(标题)
msg['Subject'] = 'Python'
#发送者
msg['From'] = Sender
#连接到SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)  #25为端口号
#登陆邮箱 邮箱名+客户端授权密码
mailServer.login(Sender, password)
#发送邮件
mailServer.sendmail(Sender, ["15279699889@163.com"], msg.as_string())  #[]中给出收件人的邮箱,数量无限
#退出邮箱
mailServer.quit()
'''
