#获取对象信息(对象类型)

#1，type()
>>> type(123)
<class 'int'>
#等价于
type(123)===int
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
#type 返回对应的变量的类型
>>>type(123)==type(456)
True
#type还可以判断函数
import types
def fn():
	pass
type(fn)

#2,isinstance()
#可以判断基本类型
instance(111,int)
#是否是一个类的子类
#判断是否是某种类型中的一种
isinstance([1,2,3],(list,tuple))
#判断[1,2,3]是不是list或tuple

#3，dir()
#获得一个对象的所有属性，方法(返回一个包含字符串的list)
dir(12)
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
'''
#dir的属性和方法应用：
len('123')
#等价于
'123'.__len__()

#测试是否有某项属性:hasattr
class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj=MyObject()
#测试obj的属性
hasattr(obj,'x')
#给对象设置属性
setattr(obj,'y','19')
#获得属性'y'
getattr(obj,'y')
obj.y
#可以传入default参数，如果参数不存在返回默认值
getattr(obj,'z',404)
#也可以通过赋值，获得对象的方法
fn=getattr(obj,'x')#把obj的方法'x'赋给fn
fn
#等价于
obj.x
#注意，这些方法应该是不知道对象信息的时候，才会去获取对象的信息

def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None
#如果fp中存在啊read方法，则这个对象是一个流，可以进行读取




