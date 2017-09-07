#-*- coding :UTF-8 -*-
#一行代码能解决的事情，绝不写五行

#1,切片:提取list，tuple中的部分元素：

L = ['UMR1','UMR2','UMR3','UMR4','UMR5']
print(L[0:3])#暂时取出来。从0到3但不包括3
print(L)
#	支持倒数取数
print(L[-2:-1])#!!!!注意倒数第一个索引时-1
#	取前3个数
print(L[:2])
#	取最后两个数
print(L[-2:])
#	复制一个list
a=L[:]
print(a)
#	前十个数，每隔两个取一个
#	字符串'asdbfh'也可以切片
a='asdfghj'[:3]
print(a)
#切片工具可以节省很多地方的循环

#2，迭代(iteration)：给定一个list或tuple，通过for来遍历list或tuple
#sample
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
#迭代key，在dict中也可以迭代value
for value in d:
	print(value)
#只要for循环作用于一个可迭代的对象，就可运行
#利用collections模块的lterable
from collections import Iterable
print(isinstance('abc',Iterable))
#result is True
print(isinstance(123,Iterable))
#result is False

#利用python实现下标循环
for i,value in enumerate(['A','B','C']):
	print(i,value)
#同时引入两个变量
for x,y in [(1,2),(2,4),(4,8)]:
	print(x,y)

#3，列表生成器
list(range(1,11))
#>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[x*x for x in range(1,11)]
#>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#注：把需要生成的元素''x*x'放在最前面
#可以加入条件/循环
[x*x for x in range(1,11) if x%2 == 0]
#>[4, 16, 36, 64, 100]
[m+n for m in 'ABC' for n in 'DEF']
#>['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
[m+n for m in (1,2,3) for n in (3,4,5)]
#>[4, 5, 6, 5, 6, 7, 6, 7, 8]
#列出文件夹中的所有文件
import os
[d for d in os.listdir('.')]
#>['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
#practice:
#把所有大写字符转换成小写
L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L if isinstance(s,str)]


#4，生成器
#在循环中不断推算出后续的元素，python中这种一边循环一边计算的机制，称为生成器
#方法一：
g=(x*x for x in range(10))
print(g)
for n in g:#通过for循环取出list
	print(n)
#	应用:
#	生成斐波那契数列
#	原始方法：
def fib(max):
	n,a,a1,b=0,0,0,1
	while n<=max:
		a=b
		b=a1+b
		a1=a
		n=n+1
		print(b)
	return 'done'
fib(5)
#可以同时给a,b赋值节省中间变量
def fib1(max):
	n,a,b=0,0,1
	while n<max:
		a,b=b,a+b
		n+=1
		print(b)
	return 'done'
fib1(5)
#由于生成list的方式与generater类似：
def fib2(max):
	n,a,b=0,0,1
	while n<max:
		#yield b#当函数定义中包括yield关键字，这个函数就是一个generator
		a,b=b,a+b
		n=n+1
		yield b
	return 'done'
#generator与普通函数的区别在于，执行到yield返回值(上面函数中，两个yield放置的位置不一样，获得的list就不同)
print(fib2(5))
#同样利用for循环获取下一个值：
for n in fib2(5):
	print(n)
#如果需要捕捉返回值需要捕获StopIteration错误：
g=fib2(5)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator returned value:', e.value)
		break
#practice:
def tri(max):
	L=[1]
	i=0
	while i < max:
		yield L
		L1=[1]
		j=0
		while j<len(L)-1:
		#for j in range(0,len(L)):
			L1.append(L[j]+L[j+1])
			j=j+1
			print('value of j is',j,'value of len(L)',len(L))
		L1.append(1)
		print('value of len(L1):',len(L1))	
		L=L1
		i=i+1

for s in tri(5):
	print(s)

def tri(max):
	L=[1]
	i,j=0,0
	while i < max:
		yield L
		L1=[1]
		#while j<len(L)-1:
		for j in range(0,len(L)-1):
			L1.append(L[j]+L[j+1])
			j=j+1
			print('value of j is',j,'value of len(L)',len(L))
		L1.append(1)
		L=L1
		i=i+1

for i in tri(5):
	print(i)

'''def triangles(lines):
    L = [1]
    n = 0
    while n < lines:
        yield L
        L1 = [1]
        for i in range(0, len(L) - 1):
            L1.append(L[i] + L[i + 1])
            i = i + 1
        L1.append(1)
        L = L1
        n = n + 1
for i in triangles(5):
	print(i)
'''	