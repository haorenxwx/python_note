python_note35网络编程UDP编程.py

TCP是通信双方都以流的形式发送数据，UDP面向无连接的协议
UDP协议，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。
虽然UDP传输数据不可靠，但是速度快，如果不需要可靠到达，使用UDP

***********
服务器端
***********

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET--IPV4， socket.SOCK--UDP, 不需要调用listen()方法，直接接受来自任何客户端的数据
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
	data, addr = s.recvfrom(1024)# recvfrom方法返回数据和客户端的地址和端口
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' %data, addr)# 调用sendto方法，把数据用UDP发给客户端

**********
客户端
**********

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))# 客户端仍然xaing
s.close()

服务器绑定UDP和TCP端口互不冲突，UDP的9999端口和TCP的9999端口可以各自绑定
