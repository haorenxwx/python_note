#-*- coding :UTF-8 -*-
#python 函数式编程
#允许把函数本身作为参数，传入另一个函数，还允许返回一个函数
#===>高度抽象的编程方法

#A:高阶函数
#1，map()
#两个传入参数：函数对象；Iterable(list,turple,dict)
def multi(x):
	a=x*x
	return a
r=map(multi,[1,2,3,4,5])
#r是一个惰性序列，需要用list计算
print(list(r))


#2，reduce()
#reduce 把一个函数作用在一个序列上
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
from functools import reduce
def add(x,y):
	a=x+y
	return a
r=reduce(add,[1,2,3,4,5,6])
print(r)

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def num(x,y):
	a=x*10+y
	return a
print(reduce(num,map(char2num,'13579')))

#practice1 intput['adam', 'LISA', 'barT'],output['Adam', 'Lisa', 'Bart']
def normalize(word):
	first=word[0].upper()
	rest=word[1:].lower()
	return first+rest
L1=['adam', 'LISA', 'barT']
L2=list(map(normalize,L1))
print(L2)

#3，filter()
#输入函数和字符串，函数依次作用于字符串的每个元素，根据返回值true/false决定保留或者丢弃
def is_odd(n):
	return n%2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7])))
#删除序列中的空字符串
#strip的用法
s=['Facebook;Google+;MySpace', 'Apple;Android']
s1=[ele.strip(' ').split(';') for ele in s]
print(s1)
#s=['A', '', 'B', None, 'C', '  ']
#s2=[ele.strip() for ele in s]
#print(s1)
def un_blank(s):
	return s and s.strip()
print(list(filter(un_blank,['A', '', 'B', None, 'C', '  '])))
#用filter求素数
def _init():
	n=1
	while True:
		n=n+2
		yield n
def not_dividible(n):
	return lambda x :x%n>0
#lambda用法：能够嵌入到其他表达式中的隐藏函数
#	在表达式中重新定义一个函数，不需要把定义和表达式分开
#	限制，只能由一条表达式去组成
#lambda x:x*x等价于
#def f(x):
#	return x*x

def prime():
	n=2
	it=_init()
	while True:
		n=next(it)
		yield n
		it=filter(not_dividible(n),it)
for n in prime():
	if n<600:
		print(n)
	else:
		break
#filter也是惰性计算，这里n表示的是全体素数

#practice,用filter过滤掉非回数
'''def _init():
	n=1
	while True:
		n=n+1
		yield n
def back(n):
	n=str(n)
	m=n[-1::-1]
	return lambda n :n==m
def prime():
	yield 1
	it=_init()
	while True:
		n=next(it)
		yield n
		it=filter(back(n),it)
for n in prime():
	if n < 500:
		print(n)
	else:
		break
还是不清楚在哪里出错了
'''

def back(n):
	n=str(n)
	m=n[-1::-1]
    #return lambda: n==m
	if m==n:
		return True
	else:
		return False

print(list(filter(back,range(12580,13580))))



#4，sort排序算法
#按照绝对值大小排队
print(sorted([36,5,-12,5,-21],key=abs))
#按照字符串长度排序
print(sorted(['gakki','umr','toda','emma'],key=str.lower))
#按照字符串长度反向排序
print(sorted(['gakki','umr','toda','emma'],key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
print(sorted(L,key=by_name))
def by_score(t):
	return t[1]
print(sorted(L,key=by_score))



#5：返回函数
#example:
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax = ax+n
		return ax
	return sum
#返回函数的好处：调用lazy_sum()时不返回求和的结果
#f=lazy_sum(1,2,3,4),调用f()时才真正计算结果
f1=lazy_sum(1,2,3,4)
print(f1())
#返回的是求和的结果
f2=lazy_sum(1,2,3,4)
print(f1,f2)
print(f1==f2)
#f1,f2的计算结果不会相互影响，f1，f2的调用分别创建了两个新函数
#每次调用函数，相关变量都储存在返回函数中，称为闭包。

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
#由于三个函数调用时没有立即执行，3个函数都返回时，他们所引用的变量i都变成3
#一定要注意，返回函数不要引入循环变量，或者后续会发生变化的变量。


#6 装饰器decorator
#装饰器： 在代码运行期间，动态的增加功能

#例1：要增加函数now的功能,在运行now()的过程中增加log：
# 原有的now()
def now():
	print('20170911')
#decorator:相当于返回函数的高阶函数：
def log(func):
	def wrapper(*args,**kw):
	#(*args,**kw)表示wrapper可以接受任意参数的调用
		print('call %s():' % func.__name__)
		#func.__name__,表示取出func的名字
		return func(*args, **kw)
	return wrapper
#log 作为装饰器，接受一个函数作为参数并且返回一个函数，利用'@log'把decorator放在函数的定义处
@log
def now():
	print('20170911')
now()

#例2：自定义log的文本(decorator本身需要传入参数)
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('20170911')
now()
print(now.__name__)
#经过装饰后的函数，__name__已经从now变成了wrapper
#所以需要把now()函数的属性(例如__name__)复制到wrapper中
#利用functools.wraps,下面是标准的decorator的写法
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
#带参数的标准写法：
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
#练习1,在函数调用前后打印出'begin call'和'end call'
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call')
		func(*args,**kw)
		print('end call')
	return wrapper
@log
def now():
	print('20170911')
now()
#练习2,支持@log, 也支持@log('execute')
def log(text):
	if callable(text):#检验是否有函数传入
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('call %s():' %text.__name__)
			return text(*args,**kw)
		return wrapper
#把所有的func都替换为text
	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text, func.__name__))
				return func(*args,**kw)
			return wrapper
		return decorator
@log
def now1():
	print('20170911')
now1()

@log('execute')
def now2():
	print('20170911')
now2()



#6，偏函数partial function
#利用functools.partial 利用现有函数的功能,通过改变默认值创建新函数
#以int()为例，设置base=N就可以做N进制的转换(把N进制数转化为十进制)：
int('100010',base=2)
#定义新函数：
import functools
int2 = functools.partial(int, base=2)
print(int2('100010'))

#总结：在函数参数太多，需要简化时使用，可以固定住原函数的部分参数，定义新函数。

#创建partial function时，可以接收：函数对象；*arg；**kw三种参数
#eg：
max2=functools.partial(max,10)
#10 作为*args参数加入到参数中。
max2(5,6,7)
#等价于
args = (10,5,6,7)
max(args)
