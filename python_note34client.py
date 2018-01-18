#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPV4&TCP
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michel',b'Tracy',b'Sarah']:
	#发送数据：
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')# 发送exit信号
s.close()