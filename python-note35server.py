#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET--IPV4， socket.SOCK--UDP, 不需要调用listen()方法，直接接受来自任何客户端的数据
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
	data, addr = s.recvfrom(1024)# recvfrom方法返回数据和客户端的地址和端口
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)# 调用sendto方法，把数据用UDP发给客户端
