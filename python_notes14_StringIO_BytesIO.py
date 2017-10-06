python_notes13_StringIO_BytesIO.py

StringIO:------>只能操作str

在内存中读取str
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('Gakki')
print(f.getvalue())#获取写入后的str
>>> hello Gakki
可以初始化一个StringIO，然后像读文件一样读取
from io import StringIO
f=StringIO('hello\nhi\ngakki!')
while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())

ByteIO:----->可以操纵二进制数据

from io import ByteIO
f=ByteIO()
f.write('中文',encoding('utf-8'))#写入的是经过UTF-8编码的byte
print(f.getvalue())


