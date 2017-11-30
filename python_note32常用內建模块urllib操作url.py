python_note32常用內建模块urllib操作url.py

urllib提供了一系列用于操作URL的功能

- request
发送get请求到指定的页面，然后返回HTTP相应

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:',f.status,f.reason)
	for k,v in f.getheaders():
		print('%s: %s' %(k,v))
	print('Data: ',data.decode('utf-8'))

如果我们想模拟浏览器发送GET请求，要使用Request对象添加HTTP头。

from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

会返回移动版的网页
