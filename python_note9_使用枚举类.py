#python_note9_使用枚举类/元类

#枚举类
#在需要定义常量时使用，定义枚举类，使每一个常量都是class的唯一一个实例，用Enum实现
from enum import Enum

Month=Enum('Month',('Jan','Feb','Mar','Apr'))
#可以用Month.Jan引用常量，枚举它的所有成员
for name,member in Month.__members__.items():
	print(name,'=>',member,',','member.value')
#member.value是给member自动赋值，从1开始计数
#如果要精确的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique
@unique
#unique装饰器可以检查有没有重复的
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=2
#报错SyntaxError: multiple statements found while compiling a single statement

#可以通过多种方式调用枚举类
Weekday.Sun#引用枚举常量
Weekday(1)
Weekday['Sun']
Weekday.Sun.value#引用枚举常量的值


#元类
#python作为动态语言，函数和类不是编译时定义的，而是运行时动态创建的
1：type()函数
	可以用来返回一个对象的类型，也可以创建新的类型
#定义函数
def fn(self,name='world'):
	print('Hello,%s.' %name)
#创建Hello class
Hello=type('Hello',(object,),dict(hello=fn))
#创建的时候type()依次传入3个参数
#1：class 名称，2：继承的父类合集，3：把方法fn跟函数名hello绑定
h=Hello()
h.hello()

2：metaclass元类
	用来控制类的创建行为，metaclass可以允许创建类或者修改类
	==基本不会用到
例1：利用Metaclass在自定义的MyList增加一个add方法
class ListMateclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']= lambda self,value:self.append(value)
		return type.__new__(cls,name,base,attrs)
class MyList(List,metaclass=ListMateclass):
	pass
#这时MyList就可以调用add()方法了
L=MyList()
L.add(1)

例2：ORM(Object Relational Mapping),对象关系映射
	把关系数据库的一行，映射为一个对象，也就是一个类对应一个表
	所有类都必须动态定义，这样使用者才能根据表的结构定义出对应的类来。
编写一个ORM框架：

1，写出调用接口：
	使用者想用ORM框架定义User类来操作对应的数据库表User：
class User(Model):
	#定义类的属性到列的映射：
	id=IntegerField('id')
	name=StringField('username')
	email=StringField('email')
	password=StringField('password')
#创建一个实例
u = User(id=12345,name='Gakki',email='gakki@orm.com',password='my-pwd')
#保存到数据库
u.save()
其中，父类Model和属性类型StringField,IntegerField是由框架提供
剩下的魔术方法如：save()由metaclass自动完成
	
2：按照接口，实现ORM
	2.1：定义Field，负责保存数据库表的字段名称和字段类型
class Field(object):
	def __init__(self,name,column_type):
		self.name=name
		self.column_type=column_type

	def __str__(self):
		return '<%s,%s>' %(self.__class__.__name__,self.name)

	2.2:根据Field，进一步定义各种类型的Field，StringField，IntegerField等
class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')
		#利用super找到多继承中的第一个父类，避免重复调用。
class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

	2.3:编写ModelMetaclass
class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model:%s' %name)
		mapping=dict()
		for k,v in attrs.items():#作用对象时字典，返回可遍历的(键,值元组数组)
			if isinstance (v,Field):
				print('Found mapping: %s ==> %s' %(k,v))
				mapping[k]=v
		for k in mapping.keys():#字典中返回所有键
			attrs.pop(k)# pop(k)表示删除列表中索引位置为k的值
						# pop()没有指定对象时删除最后一个
		attrs['__mapping__']=mappings #保存属性和列的映射关系
		attrs['__table__']=name #假设表名和类名一致
		return type.__new__(cls,name,bases,attrs)

	2.4:编写基类Model：
class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model'object has no attribute '%s'" %key)

	def __setattr__(self,key,value):
		self[key]=value
	    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))