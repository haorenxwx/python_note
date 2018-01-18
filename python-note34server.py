#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))	#因为服务不是标准服务，所以用9999端口，小于1024的端口号必须要有管理员权限
s.listen(5)	#用listen()方法监听端口，传入的参数指定等待链接的最大数量
print('waiting for connection')
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
while True:
	sock, addr = s.accept()
	#接受一个新链接
	t = threading.Thread(target=tcplink, args =(sock, addr))
	#创建新线程处理TCP连接
	t.start()
