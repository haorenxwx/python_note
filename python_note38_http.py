python_note38_http协议.py

HTTP:浏览器和服务器之间通信，在网络上传输HTML协议
HTML:用来定义网页的文本


HTTP请求流程：

1：浏览器向服务器发送HTTP请求
	- get（仅请求资源）/post（还附带用户数据）
	- full url path
	- 域名和其他先关header
	常见的HTTP方法：
		- get:服务器向客户端发送命名资源
		- post:把客户端数据发送到服务器网管应用程序中
2：服务器向浏览器返回HTTP响应
	- 响应代码 eg:200
	- 响应类型
	- 内容 body
3：如果浏览器还要继续请求图片等其他资源，再次发送HTTP请求，重复1，2

web采用的http协议采用非常简单的请求响应模式：
	编写一个页面只需要在http请求中把http发送出去，不需要附带图片，视频等。
	浏览器如果要请求图片视频，会发送另一个http请求（事物）
	- 一个HTTP请求一次只处理一个资源
HTML可以链入其他服务器的资源（一个站点链接到另一个站点）WWW


HTTP格式：
Get:
GET /path HTTP/1.1（表示协议版本）
Header1: Value1
Header2: Value2
Header3: Value3
\r\n换行
（get 没有主体，因为）

Post:
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
\r\n\r\n

body data goes here...

HTTP响应：
200 OK
Header1: Value1
Header2: Value2
Header3: Value3
\r\n\r\n
body data goes here...

Body的数据类型由Content-Type头来确定
	网页：文本
	图片：二进制数据
Content-Encoding: gzip 需要将body数据解压缩得到真正的数据，减少body大小，加快传输速率

HTTP在向服务器发送报文之前，需要用internet protocol和端口号在客户端和服务器之间建立一条TCP/IP连接
http://10.2.200.231:8888
通过DNS（domain name server将主机名转移到IP地址）在没有端口号时，假设默认端口号是80
浏览器访问流程：
	- 浏览器解析主机名
	- 浏览器将主机名解析成IP地址/port
	- ...与服务器建立TCP连接
	- ...向服务器发送请求报文
	- 服务器回送响应报文
	- 关闭链接，浏览器显示文档

Telnet:
	将键盘连接到某个端口的TCP链接，常用于远程终端会话，
	可以连接包括 HTTP服务器在内的所有TCP服务器
	web服务器将telnet作为一个web客户端处理，所有会送给TCP连接的数据都会直接显示在屏幕上

web结构组件：
	代理：客户端和服务器之间的HTTP实体，用于转发请求，
		对请求和响应做出过滤
	缓存（web cache&proxy cache: HTTP仓库，将常用页面副本保存在立客户端更近的地方
		客户端从附近缓存下载文档会比远程web server下载快速
	gateway: 连接其他应用程序的特殊web服务器
		通常用于将HTTP流量转化为其他协议，
		如HTTP/FTP网关： 通过HTTP请求接受对FTP URI的请求
						通过HTTP请求接受对FTP协议获取文档，并封装成HTTP报文
	隧道（tunnel）：建立后，对原始数据进行盲转发的HTTP应用程序
		如HTTP/SSL隧道：通过HTTP连接承载加密的SSL流量	
	agent代理：代表用户发起HTTP请求的客户端程序（如：web 浏览器，自动搜索引擎“网络蜘蛛”）
					
