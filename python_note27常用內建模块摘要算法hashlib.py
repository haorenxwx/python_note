python_note27常用內建模块摘要算法hashlib.py

摘要算法：又叫做哈希算法，散列算法。python中提供MD5，SHA1
		通过一个函数，把任意长度的数据转换为长度固定的字符串digest（摘要）（16进制字符串）
		计算f（data）很简单，但是用digest反推data非常困难

摘要算法MD5为例：
	import hashlib

	md5 = hashlib.md5()
	md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
	print(md5.hexdigest())
  如果数据量很大，可以分块多次调用
	import hashlib

	md5 = hashlib.md5()
	md5.update('how to use md5'.encode('utf-8'))
	md5.update('in python hashlib?'.encode('utf-8'))
	print(md5.hexdigest())
  计算结果一样

SHA1算法举例：
	import hashlib
	sha1 = hashlib.sha1()
	sha1.update('how to use sha1 in'.encode('utf-8'))
	sha1.update('python hashlib'.encode('utf-8'))
	print(sha1.hexdigest())

摘要算法应用：
	通过储存用户口令的摘要，储存登录网站的用户名和口令
	利用输入的明文口令的MD5和数据库中的MD5对比，如果一致，说明口令输入正确
	import hashlib
	from collections import defaultdict

	def calc_md5(username,password):
		md5 = hashlib.md5()
		code = md5.update(password.encode('utf-8'))
		#print(md5.hexdigest())	
		dd = defaultdict(lambda: 'N/A')
		dd[username] = code
		print(dd)

	if __name__=="__main__":
		username = input("Please input username")
		password = input("Please input password")

	因为用户有可能使用简单口令，黑客可以通过常用口令得到反推表，
	对简单口令加强保护，可以对原始口令加一个复杂字符串实现。
	def calc_md5(password):
		return get_md5(password + 'the_salt')
	def get_md5(password1):
		md5 = hashlib.md5()
		code = md5.update(password1.encode('utf-8'))
		return code
注意，摘要算法不能用于加密，因为无法通过摘要反推明文， 只能用于防篡改





