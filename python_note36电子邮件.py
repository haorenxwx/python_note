python_note36电子邮件.py

MUA：Mail User Agency 邮件用户代理,例如Outlook或者Foxmail
MTA: Mail Transfer Agency 邮件传输代理，例如网易，新浪等email服务商，email会被投递到网易提供的MTA，再由网易投到新浪的MTA
MDA：Mail Deliver Agency 邮件投递代理，email到达后，静静地躺在新浪的某个服务器里，存放在某个文件，或特殊的数据库里，这个长期保存的地方称为电子邮箱

发送邮件过程：
	发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

编写程序发送和接收邮件实际上就是
1：编写MUA把邮件发到MTA； MUA -> MTA 和 MTA -> MTA 使用SMTP（simple mail transfer protocol）

2: 编写MUA从MDA收邮件： 使用两种协议
	POP: Post Office Protocal （目前使用POP3）
	IMAP: Internet Message Access Protocal




SMTP发送邮件

- SMTP是发送邮件的协议，发送纯文本，HTML, 和带附件的邮件
- python支持两个模块： email负责构造邮件，smtplb发送邮件
- 邮件主题，发件人，收件人等信息是包含在发给MTA的文本中的，
	要把From To Subject添加到MIMEText

from email import encoders
from email.header import header
from email.utils import parseaddr, formataddr
from email.mime.text import MINEText

import smtplib
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#MINEText第一个参数是邮件正文，第二个参数是MIME的subtype,'plain'表示纯文本
#最后一定用Utf-8编码，保证多语言兼容性

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name, 'ntf-8').encode(),addr))
	然后通过SMTP发送出去：
#输入Email地址和口令：
from_addr = input('From')
password = input('Password')
#输入收件人地址：
to_addr = input('To: ') #多个地址用','分隔
#输入SMTP服务器的地址：
#常用服务器地址端口：http://blog.csdn.net/hssdw25172008/article/details/8729469
smtp_server = input('SMTP server: ')



server = smtplib.SMTP(smtp_server,25)#SMTP协议默认端口25
server.set_debuglevel(1)#打印SMTP服务器交互的所有信息
server.starttls() #for gmal, need this line to enable
server.login(from_addr, password)#用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())
#发邮件，因为一次可以发给多个人，所以传入一个list；as_string()把MINEText对象变成str
server.quit()

发送HTML邮件：
更改MIMEText对象
msg = MIMEText('<html><body><h1>Hello</h1>' + 
	'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
	'</body></html>', 'html','utf-8')


