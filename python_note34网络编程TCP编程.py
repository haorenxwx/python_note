python_note34网络编程TCP编程.py

Socket用来打开网络链接，需要知道目标计算机的IP地址和端口号，再指定协议类型

************
客户端：
************
大多数俩呢及都是可靠的TCP链接，创建链接时，主动发起链接的叫客户端，被动相应链接的叫服务器

import socket

1,创建一个socket链接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#创建一个socket
#AF_INET指定使用IPv4协议，如果要用IPv6就要指定为AF_INET6
#SOCK_STREAM 指定面向流的TCP协议

2，链接服务器
s.connect(('www.sina.com.cn',80))	参数是一个turple， 包含地址和端口号
#作为服务器，提供什么样的服务，端口号就必须固定下来，
	80:web服务的标准端口
	25：SMTP服务
	21：FTP服务
	端口号小于1024的是Internet标准服务的端口，端口号大于1024的可以任意使用。

3，发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#发送数据
	TCP创建双向链接，双方都可以给对方发送数据
	HTTP协议规定客户端必须先发送请求给服务器，服务器收到后才发送数据给客户端。

4，接受数据
#接收数据
buffer = []
while True:
	#每次最多接受1k字节：
	d = s.recv(1024)
	if d:#反复接受，直到recv()返回空数据，表示接收完毕
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

5，关闭链接
s.close()
	#关闭链接
	接收到的数据后 用close()方法关闭Socket，一次完整的网络通信结束了

6，保存数据
header, html = data.split(b'\r\n\r\n',1)#把http头和网页分离
print(header.decode('utf-8'))#打印http头
with open('sina.html','wb') as f:
	f.write(html)	#把网页内容打印到sina.html

************
服务器
************
服务器进程，需要绑定一个端口，监听来自其他端口的链接。
如果有客户端链接，服务器与客户端进行socket建立链接，随后的通信依靠这个socket链接
- 一个socket依赖： 服务器地址，服务器端口，客户端地址，客户端端口来确定唯一的socket

1，创建socket链接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

2，绑定监听地址端口
	- 服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上
	- 用‘0.0.0.0’ 绑定到所有的网络地址上
	- 用’127.0.0.1‘ 绑定本机地址（绑定本机地址，客户端必须同时在本机运行才能链接，外部计算机无法进入）
s.bind(('127.0.0.1', 9999))	#因为服务不是标准服务，所以用9999端口，小于1024的端口号必须要有管理员权限
s.listen(5)	#用listen()方法监听端口，传入的参数指定等待链接的最大数量
print('waiting for connection')

3，服务器程序通过永久循环，接受客户端链接，accept()会等待并返回一个客户端的连接
while True:
	sock, addr = s.accept()
	#接受一个新链接
	t = threading.Thread(target=tcplink, arg = (sock, addr))
	#创建新线程处理TCP连接
	t.start()
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'welcome!')# 建立连接以后，服务器发送欢迎信息
	while True:
		data = sock.recv(1024)# 等待客户数据
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':# 如果客户发送了exit字符串，直接关闭连接。
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s: %s closed.' % addr)
	
******
编写与服务器程序对应的客户端程序
******

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPV4&TCP
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michel',b'Tracy',b'Sarah']:
	#发送数据：
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')# 发送exit信号
s.close()





