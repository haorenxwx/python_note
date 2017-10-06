python_notes13_文件读写.py

在磁盘上读写文件的功能都是由操作系统提供的
读写文件实际上是请求操作系统打开一个文件对象
通过操作系统提供的接口进行读写

读文件
1：读取UTF-8编码的文本文件
f=open('/User/michael/test.txt','r')
f.read()
f.close()#使用完必须关闭，因为文件对象会占用操作系统的资源
因为文件读写时都会产生IOError，后面f.close就不回调用，为了避免这种情况发生,可以
	1：try...finally
try:
	f=open('/path/to/file','r')
	print(f.read())
finally:
	if f:
		f.close()
	2：引用with语句自动调用close()方法
with open('/path/to/file','r') as f:
	print(f.read())
因为'read()'会一次性读取文件的全部内容，如果文件有10G，内存就爆了
用'read(size)'可以限制每次最多读取size个字节的内容
用'readlinez()'一次性读取所有内容并按行返回list

这样像'open()'函数返回，有'read()'方法的对象，如：字节流，网络流，自定义流


2：读取二进制文件，如图片，视频
f=open('/Users/michael/test.jpg','rb')
f.read()
#输出为16进制的数据

3：读取非UTF-8编码的文本文件，需要给'open()'传入encoding参数，如读取GBK编码的文件。
f=oepn('/Users/michael/gbk.txt','r',encoding='gbk')
f.read()
当编码不规则时，可能遇到UnicodeDecodeError，可以忽略错误
f=open('/Users/michael/gbk.txt','r',encoding='gbk',errors='ignore')

写文件
与读类似，传入'w'或'wb'表示写文本，或二进制文件
f =open('/Users/michael/gbk.txt','w')
f.write('Hello Gakki')
f.close()
或
with open('/Users/michael/gbk.txt','w')as f:
	f.write('Hello Gakki')
要写入特定编码的文本，给'open()'传入encoding参数，把字符串转换为指定编码

