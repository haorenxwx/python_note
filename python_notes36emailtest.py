#!/usr/bin/python
# -*- coding: utf-8 -*-


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#from_addr = input('From: ')
from_addr = r"xuwanxin69@gmail.com"
#password = input('Password: ')
password = r"Buaaee@702"
#输入收件人地址：need to add "xuwanxin69@163.com"
to_addr = "xuwanxin69@163.com"
#to_addr = input('To: ')
#输入SMTP服务器的地址：
#常用服务器地址端口：http://blog.csdn.net/hssdw25172008/article/details/8729469
#smtp_server = input('SMTP server: ')
smtp_server = "smtp.gmail.com"

msg = MIMEText('hello, send by Python...','plain','utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('想不到吧我又来了……', 'utf-8').encode()



server = smtplib.SMTP(smtp_server,587)#SMTP协议默认端口25
server.starttls()
server.set_debuglevel(1)#打印SMTP服务器交互的所有信息

server.login(from_addr, password)#用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())
#发邮件，因为一次可以发给多个人，所以传入一个list；as_string()把MINEText对象变成str
server.quit()

'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "xuwanxin69@gmail.com"
my_password = r"Buaaee@702"
you = "xuwanxin69@163.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()
'''