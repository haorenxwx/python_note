#面向对象高级编程
python作为动态语言，可以给实例绑定任何属性和方法。
#定义class
class Student(object):
	pass
#给实例绑定属性
s=Student()
s.name="gakki"
print(s.name)
#给实例绑定方法
def set_age(self,age):#定义一个函数作为实例方法
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)#调用实例方法
s.age#测试结果

#给实例绑定方法，对另一个实例不起作用，
s2=Student()
s2.set_age(25)
#error--------

#如果要给所有实例绑定方法，可以给class绑定方法
def set_score(self,score):#定义函数作为绑定class的实例
	self.score=score
Student.set_score=set_score#给class绑定方法
#所有实例都可以调用这个方法
s2.set_score(25)




使用__slots__,限制给类添加的属性
class Student(object):
	__slots__=('name','age')#用turple定义允许绑定的属性名称
s=Student()
s.name='gakki'
s.score='100'
#error---------

#__slots属性对当前类的实例起作用，对继承的子类不起作用。除非子类中也有定义__slots




@property 装饰器
#为了限制调用类的方法时，设置的参数的范围。可以通过get_score获得参数，set_score检查参数
class Idole(object):
	def get_score(self):
		return self._score
	def set_score(self,score):
		if not isinstance(score, int):
			raise ValueError("score must be integer")
		if 0>score or score>100:
			raise ValueError("score must between 1-100")
		self._score=score
a=Idole()
a.set_score(60)
a.get_score()
#这样做相对复杂，利用装饰器@property可以简化
class Idole(object):
	@property#把get_score方法变成属性
	def score(self):
		return self._score

	@score.setter#创建另一个装饰器，负责吧setter方法变成属性赋值
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("score must be integer")
		if 0>value or value>100:
			raise ValueError("score should between 0-100")
		self._score=value
a=Idole()
a.score=60
a.score
#利用@property，我们在操作实例属性时，实例属性并不是直接暴露的，而是通过getter和setter方法实现的

#当只定义getter方法，不定义setter方法时，就是一个只读属性
class Student(object):
	@property
	def birth(self):
		return self.birth
	@birth.setter
	def birth(self,value):
		self._birth =value
	@property
	def age(self):
		return 2017-self._birth
#age可以通过birth计算,设为只读
a.birth=1997
a.age
#练习
class Screen(object):
	def width(self,value):
		self._width=value

	def height(self,value):
		self._height=value
	@property
	def resolution(self):
		return self._width*self._height
#这时会报错说，No Attribute Named _width
#因为，_width和_height是私有变量，必须要在方法内return才能在其他方法中调用
#修改为
class 
class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width=value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height=value

	@property
	def resolution(self):
		return self._width*self._height
TV=Screen()
TV.width=1024
TV.height=768
print(TV.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution



多重继承
#一个子类可以继承多个父类
class Animal(object):
	pass
class Runnable(object):
	def run(self):
		print("Running")
class Dog(Animal,Runnable):
	pass
#子类Dog可以同时获得两个父类的功能
一般继承关系里，主线都是一脉相承的，如果要给子类加入额外功能功能，这种继承的设计叫MixIn
更改为
class RunnableMixIn(object):
	pass
class Dog(Animal,RunnableMixIn):
	pass
父类有重复的方法，先继承生父的
#生父
class Father():

    def func(self):
        print('生父打儿子')
#隔壁老王
class LaoWang():

    def func(self):
        print('老王打儿子')
    def func1(self):
        print('跟你妈说明天下午我会来')
#继父
class StepFather():

    def func(self):
        print('继父打儿子')
    def func1(self):
        print('我还会打你妈')
#神秘人
class Mysterious(Father,LaoWang,StepFather):
    pass
##让我们看看到底谁打了儿子
s=Mysterious()
s.func()
s.func1()



定制类（__slots__这样形式的变量或函数名，在python中都有特殊的作用。）
#例1：__str__
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
print(Student('Gakki'))
#__str__目的是返回用户看到的字符串，所以还需要通过print()显示
#如果要直接显示,用：__repr__

class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__=__str__#__repr__用来给程序员调试用
Student('Gakki')
>>>Student object (name: Gakki)


#例2：__iter__
#如果一个类被用作 for...in循环，就必须实现__iter__()方法。
#for循环调用
class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
		#初始化计数器a,b
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a > 10000:
			raise StopIteration
		return self.a
for n in Fib():
	print(n)


#例3：__getitem__()
#使类像列表一样，可以提取其中的任意一项。
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
f=Fib()
f[0]
#list可以做切片：
list(range(100))[5:10]
#但是对于Fib()，这样的操作会报错，__getitem__()传入的参数可能是一个int，也可能是一个slice
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>= start:
					L.append(a)
				a,b=b,a+b
			return L
>>>f=Fib()
>>>f[0:5]
[1, 1, 2, 3, 5]
#加入一个isinstance的判断，把int和slice分开就可以做切片了
#通过这样的方法，定义的类可以表现的python自带的list，tuple，dict没有任何区别

#例4：__getattr__
#可以动态返回属性
#返回值
class Student(object):
	def __init__(self):
		self.name='Gakki'
	def __getattr__(self,attr):
		if attr=="score":
			return 99
>>>s=Student()
>>>s.score
#返回函数
class Student(object):
	def __init__(self):
		self.name="Gakki"
	def __getattr__(self,attr):
		if attr=="score":
			return lambda: 25
>>>s=Student()
>>>s.name
Gakki
>>>s.score()
25
>>>s.abc#如果要调用任意值，默认返回值None，如果要返回正常错误，要加一行raise
class Student(object):
	def __init__(self):
		self.name="Gakki"
	def __getattr__(self,attr):
		if attr=="score":
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#可以报指定的错误
#通过完全动态的__getattr__,通过链式调用，可以完全动态化处理类的属性和方法。
class Chain(object):
	def __init__(self,path=''):
		self._path=path
	def __getattr__(self,path):
		return Chain('%s/%s'%(self._path,path))
	def __str__(self):
		return self._path

	__repr__=__str__
>>>Chain().status.user.timeline.list
#链式调用：一个语句多次调用类的一个或者多个方法
#例如：
p=Person()
p.name("Gakki").age(29).score(100)


#例5: __call__
#调用实例方法时通常用instance.method()
#定义了__call__以后就可以直接调用实例
class Student(object):
	def __init__(self,name):
		self.name=name
	def __call__(self):
		print('The best idole %s.'%self.name)
d=Student('Gakki')
d()
#此时，d可以被调用
>>>callable(d)
True
#没有定义__call__方法时，实例d就不能被调用，callable结果显示false


