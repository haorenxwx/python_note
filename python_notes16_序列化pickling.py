python_notes16_序列化pickling/Json

把变量从内存中，变成可传输或者传输的过程，称作序列化。
序列化之后就可以吧序列化以后的内容写入磁盘，或者通过网络传输到别的机器上


通过pickle模块实现

import pickle
d=dict(name='Gakki',age=29,score=100)
pickle.dumps(d)
>b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x1dX\x05\x00\x00\x00scoreq\x02KdX\x04\x00\x00\x00nameq\x03X\x05\x00\x00\x00Gakkiq\x04u.'
可以把任意对象序列化成一个bytes，然后把bytes写入文件

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()
此时dump.txt保存的是pickle序列化出的对象
可以pickle.load()反序列化出对象

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
注：pickle因为兼容性差，最好用于保存不重要的数据

如果要在不同的编程语言中传递对象，需要把对象序列化为标准化格式：Json
Json表示出来是一个字符串，可以被所有语言读取，可以方便的储存到磁盘或者通过网络传输
python内置模块json提供了完整的python到json的转换：


通过Json实现
import json
d = dict(name="Gakki",age=29,score=100)
b=json.dumps(d)

把json反序列化为python对象，用loads或load方法
json_str='{"age":20,"score":88,"name":"Bob"}'
json.loads(json_str)
因为Json标准规定的编码是UTF-8，所以python的str和Json中的数值总能正确的转换

Json进阶：定义类，然后序列化
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('Gakki',29,100)
print(json.dumps(s))
此时会报错，因为类Student不是一个可序列化的json对象

这时需要
1：写一个函数把dict传进去
2：设置json.dumps的默认参数
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
	def student2dict(str):
		return {
			'name':std.name,
			'age':std.age,
			'score':std.score
		}
s=Student('Gakki',29,100)
print(json.dumps(s,default=student2dict))

但是这样如果再有一个新的class，就还是不能序列化为json实例，
利用default参数设置可以把任意class的实例变成dict：

print(json.dumps(s,default=lambda obj: obj.__dict__))
每一个class的实例都有__dict__属性，就是一个dict，用来储存实例变量
例外：定义了__slot__的class


如果要把dict转化为Student实例对象：
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
json_str='{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))
打印出来的就是Student的实例对象




