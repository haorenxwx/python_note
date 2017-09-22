#面向对象编程


类和实例
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

#因为类起到模板作用，创建实例时，需要把我们认为必须绑定的属性强制写进去
#通过定义__init__方法，在创建实例的时候就把name，score等属性绑定上去
__init__方法的第一个参数一定是self，表示创建的实例本身
在init方法内部可以把各种属性绑定到self
这样创建实例的时候不能传入空参数，必须传入和__init__方法匹配的参数
(不需要传self python解释器会把自己的变量传进去)


	def print_score(self.name,self.score):
		print('%s:%s' % (self.name,self.score))
#Student: 就是一个对象
#对象有name和score两个属性
#对象内的关联函数就是对象的方法

bart = Student('Bart Simpson',59)
bart.print_score()
#这时内部变量可以被调用和更改：
bart.score
>>>59
bart.score=60


访问限制
#如果希望内部变量的属性不被外部变量访问，可以在实例变量名前加__
#注__name是private变量，__name__不是
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s:%s' % (self.__name,self.__score))
#此时变量内容不能改变和访问
bart.__score
>>>error
#这时如果需要访问，应该增加get_name和get_score的方法
class Student(object):
	...
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
bart.get_name

#如果需要对变量进行修改，增加set_score方法，可以做参数检查，避免传入无用的参数
	...
	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
bart.set_score(150)
#就会报错


继承和多态
class Animal(object):
	def run(self):
		print("the animal is running")
class Cat(Animal):
	pass
class Dog(Animal):
	pass
#Animal称为父类(Basa class,Super class)
#Cat 和Dog称为子类(Subclass),继承了Animal中的全部方法
>>>a=Cat()
>>>a.run()
the animal is running
>>>Cat().run()
#子类可以增加方法
class Cat(Animal):
	def eat(self):
		print("Cat is eating")
#当子类和父类存在相同方法时，会调用子类的方法
class Dog(Animal):
	def run(self):
		print("dog is running")
>>> a=Dog()
>>> a.run()
dog is running

#多态
>>>a=list()
#用isinstance()判定变量是否是某个类型
>>>isinstance(a,list)
True
>>>c=Dog()
>>>isinstance(c,Dog)
True
>>>isinstance(c,Animal)
True
#在继承关系中，一个数据类型是某个子类，那数据类型也是某个父类。反过来不行

#一个函数接受Animal类型
def run_twice(animal):
	animal.run()
#可以分别传入Animal()和Dog()
run_twice(Animal())
#相当于输入了Animal().run()
run_twice(Dog())
#若新增加一个子类
class Tortoise(Animal):
	def run(self):
		print("Tortoise running slowly")
#可以直接用run_twice调用
run_twice(Tortoise())
#不需要对原函数，原类做任何的修改。只要是Animal类或是子类，都可以自动调用实际类型的run()方法


#静态语言和动态语言的区别：
静态语言，如java，需要传入Animal类型，那传入与的对象必须是animal或他的子类
动态语言，如python，只需要传入的对象有一个叫做run的方法就可以了
class Timer(object):
	def run(self):
		print("start.....")
run_twice(Timer())
由于这样的特性，继承对于动态语言不像静态语言是必须的。








