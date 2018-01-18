python_note40_WSGI接口.py

web应用的本质就是：
1：浏览器发送HTTP请求
2：服务器收到请求并生成HTML文档
3：HTML文档作为HTTP的响应body发送给浏览器
4：浏览器收到HTTP响应，从HTTP body取出html文档并显示

通过统一端口WSGI处理TCP链接，HTTP原始请求和响应格式

def application(environ, start_response):
	#environ: 一个包含所有HTTP请求的dict对象
	#start_reponse: 一个发送HTTP响应的函数
	start_response('200 OK',[('Content-Type','text/html')])
	#发送HTTP响应的Header,
	#start_response接收两个参数：
		#HTTP响应码：'200 OK'
		#一组list表示HTTP Header: '[('Content-Type','text/html')]' 
	return [b'<h1>Hello,web!</h1>']
	#函数的返回值，作为HTTP响应的Body发送给浏览器


在WSGI接口下，HTTP请求的所有输入 都可以通过environ获得
			HTTP响应的输出都可以通过start_response和函数返回值作为Body
			
