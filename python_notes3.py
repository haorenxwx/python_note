#-*- coding :UTF-8 -*-
#python 函数式编程
#允许把函数本身作为参数，传入另一个函数，还允许返回一个函数
#===>高度抽象的编程方法

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
#输入函数和字符串，

