python_note24常用內建模块base64.py

Base64 是一种用64个字符表示任意二进制数据的方法（最常见的二进制编码方法）
常用于在URL，Cookie，网页中传输少量的二进制数据

- 准备64个字符的数组
- 对二进制数据进行处理，每三个字节（8bit）一组，3*8=24 bit
- 化为四组，每组6个bit，得到4个数字作为索引，查表，获得相应的4个字符，就是编码以后的字符串
- Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%
- 如果要编码的二进制数据不是3的倍数，最后会剩下一个或两个字节，
	Base64用'\x00'字节在末尾补足后，在末尾加一个或两个’=‘表示补了多少字节

>>> import base64
>>> base64.b64encode(b'binary\x00string')
b'YmluYXJ5AHN0cmluZw=='
>>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
b'binary\x00string'

’=‘字符可能出现在Base64编码中，但是在URL和Cookie中可能会造成歧义很多Base64编码后会把=去掉

#一个能去掉=的base64的解码函数
#-*- coding: utf-8 -*-
import base64
def safe_base64_decode(s):
	if lens(s)%4 == 0:
		return base64.b64decode(s)
	else:
		while(len(s)%4 !=0 ):
			s = s + b'='
			return base64.b64decode(s)


