python_note26常用內建模块struct.py

python 没有专门处理字节的数据类型，b'str'可以表示字节，故字节数组=二进制str
python 提供了struct模块来解决bytes和其他二进制数据类型的转换

struct的pack函数把任意数据类型变成bytes：
	import struct
	struct.pack('>I',10240099)
'>'表示字节顺序是big-endian（means big end'the most significant value' is stored first--at the lowest storage address
'I'表示4字节无符号整数
'10240099'参数要和指令数据一致

unpack把bytes变成相应的数据类型
	struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
'>IH'把后面的bytes依次变为  I:4字节无符号整数， 和H:2字节无符号整数

官方文档：https://docs.python.org/3/library/struct.html#format-characters

windows位图文件（.bmp）
	s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
	struct.unpack('<ccIIIIIIHH', s)

eg:检查任意文件是否是位图文件，如果是，打印出图片大小和颜色散
用unpack读取后，‘BM’表示windows位图，‘BA’表示OS/2位图(b'B',b'M',...)

	import struct
	def check(path):
		with open(path,'rb') as f:
			inf = f.read(30)
		bmp_list = struct.unpack('<ccIIIIIIHH',inf)
		if bmp_list[0:2] == (b'B',b'M'):
			print('It is the windows bmp! And the size is %s, color number is %s' %(bmp_list[7],bmp_list[9]))
		else:
			print('It is not windows bmp!')

