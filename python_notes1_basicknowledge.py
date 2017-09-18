#!/usr/bin/python
#!/usr/bin/env python3
#让linux知道这是一个可执行文件，windows会自动跳过句

# -*- coding :UTF-8 -*-


'''print "-----------if application--------"
flag = False
name = 'UMR'
if name == 'xiaomai':
	print 'welcome xiaomai'
	flag = True
else:
	print name



print "-----------while application"
numbers = [12,13,14,15,16,17,57]
while len(numbers) > 0:
	number = numbers.pop()
	if (number % 2 ==0):
		print number
	else:
		print "that is odd number"




print "-----------for application-----------"
print "eg of 'for'1"
for letter in 'python':
	print 'Letter\n', letter
fruits = ['a','b','c']
for fruit in fruits:
	print fruit
	'''

print("eg of for 2")

idol = ['UMR1','UMR2','UMR3','UMR4']
i=0
for index in range(len(idol)):
	print(idol[i]+"is the best idol")
	i=i+1






'''print "-----------rock, paper, scissors------"
import random
start = raw_input('Are you ready for the game? Y/N')
while (start == 'Y'):
	print 'okay lets begin'
	s = int(random.randint(1,3))
	if s == 1:
		ind = 'rock'
	elif s == 2:
		ind = 'paper'
	elif s == 3:
		ind = 'scissors'
	m = raw_input('Input rock/paper/scissors or endgame')
	if (m == ind):
		print 'this is a tie'
	elif (m == 'paper'and ind == 'rock') or (m == 'rock' and ind == 'scissors') or (m == 'scissors' and ind == 'paper'):
		print 'congraduations you win '
	elif (m == 'rock'and ind == 'paper') or (m == 'paper' and ind == 'scissors') or (m == 'scissors' and ind == 'rock'):
		print 'what a pity, try again'
	elif (m == 'endgame'):
		break
	else :
		print 'Please input rock/paper/scissors or endgame'
'''

# 冒泡排序 
array = [9,7,4,8,6,2,5,1]
L=len(array)
for i in range(L):
	for j in range(L-i):
		if array[L-j-1] < array[L-j-2]: #for the index started from 0
			array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
print(array)
#取列表中末尾数
print(array[-1]) 

#增加列表元素
array.append(20)
print(array)

#删除列表元素
array.pop() #删除末尾元素
print(array)
array.pop(2) #删除第3个元素
print(array)

#替换元素
array[2]=20
print(array)

#二维列表
s=['python','java',['php','asp'],'scheme']
print(s[2][1]) #print 'asp'

'''
height=float(input('Please input your height(cm):  '))
weight=float(input('Please input your weight(kg):  '))
BMI=height/weight**2
if BMI<18.5:
	print('too light')
else:
	print('too heavy')
'''


#python_dict(dictionary)
#利用key-value进行mapping
d={'UMR':97,'gakki':99,'shiyuan':96}
print(d['UMR'])

#在dict中加入新值
d['toda']=95
print(d)

#由于key不存在时会报错，故检测key是否存在
#用in来检测
if 'angela' in d :
	print(d['angela'])
else:
	print('angela not in d')
#用get检测
d.get('gakki')
#指定返回值
d.get('gakki',-1)

#删除key
d.pop('toda')
#1，dict存放顺序和key放入的顺序没有关系
#2，占用大量内存，查找和插入顺序极快
#3，dict根据key来计算value的算法称为哈希算法(hash)，value不能变化


#python_set
#set是一组key的合集，不储存value，key也不重复
s=set([1,1,2,2,4,4])
print(s)
#增加set
s.add(5)
#删除
s.remove(5)
#与dict类似的，要使用不可变对象作为key
s.add((1,2,3))
print(s)
#turble是不可变的，可以作为key放入
#s.add((1,2,[2,3]))
#print(s)
#报错：unhashable type list



#python调用函数
#绝对值
abs(-21)
#最大值
max(2,4,5,6,7)
#数据类型转换
int('123')
float('12.23')
str(1.23)
bool(1)
hex(123)
print(hex(123))
#结果是false

#自定义函数
def myabs(x):
	if x >= 0:
		return x
	else:
		return -x
print(myabs(-21))


#可以用pass占位，让代码先运行起来
#if age >= 18:
#	pass

#返回多个值
import numpy as np
import math
#both support cos/sin calculation
def move(x,y,step,angle=0):
#angle=0,是默认参数，当没有设置angle的值得时候，默认为2.
	nx = x + math.cos(angle)
	ny = y + np.sin(angle)
	return nx,ny
#返回多个值，实际上是一个tuple
r = move(100,100,60,math.pi/6)
print (r)

#practice:
def quadratic (a,b,c):
	x=-b+math.sqrt(b**-4*a*c)
	y=-b+math.sqrt(b**-4*a*c)
	return(x,y)
answer=quadratic(1,2,1)
print(answer)

#默认参数：
#	默认参数应该在位置参数后定义。
#	默认参数所有的值应该为固定变量，否则多次迭代时会出错
def add_end(L=[]):
	L.append('End')
	return L
a=add_end()
print("first irration result when default value is '[]': "+str(a))
b=add_end()
print("second irration result when default value is '[]': "+str(b))


def add_end(L=None):
	if L==None:
		L=[]
	else:
		L.append('End')
c=add_end()
print("first irration result when default value 'None': "+str(c))
d=add_end()
print("second irration result when default value 'None': "+str(d))


#可变参数传入函数
#1，把参数作为list或者tuple传入
def calsum(numbers):
	sum=0
	for n in numbers:
		sum=sum+n
	return sum
a=calsum([1,2,3])#as list
print(a)
b=calsum((1,2,3))#as turple
print(b)
#2, 直接定义可变参数函数
def calsum1(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n
	return sum
a=calsum1(1,2,3)
print(a)
#	若已知已经有一个list或者turple
number=(1,2,3)
b=calsum1(*number)
print(b)
#可以有一种繁琐的写法= =
c=calsum1(number[0],number[1],number[2])
print(c)


#关键词参数 **+anyword
#可以传入0个或任意个参数名的参数，作为输入参数的扩展,以dic的形式储存在anyword中
#eg
def person(name, age, **kw):
	print("name is:",name,"age is:",age,"other:",kw)
	#可以只传入必要参数name和age，也可以传入其他参数，保存在kw中
personinfo=person('gakki',29,height=170,score=100)
print (personinfo)
#running result>name is: gakki age is: 29 other: {'height': 170, 'score': 100}  
#在已经存在dic数据时，也开始直接传入dic类型的变量
gakki={'height':170,'score':100}
personinfo=person('gakki',29,**gakki)
print(personinfo)

#命名关键字参数*，+关键字
def person(name,age,*,height,score):
	print ('name is:',name,'age is',age, height, score)
personinfo=person('gakki',29,height=170,score=100)
#height和score是关键字参数，如果输入的参数不是height和score，都被当做位置参数
#person(gakki,29,month=6) 会报错

#关键字参数和命名关键字参数可以重合使用
def person(name,age,*args,**kw):
#*args接受一个tuple，kw接受一个dic.建议使用惯用写法
	pass


#python 递归函数
#sample：
def multi(n):
	if n==1:
		return 1
	return n*multi(n-1)
a=multi(5)
print(a)
#计算机中函数调用通过栈stack来实现，每进入一个函数调用，就会加一层栈帧
#由于栈的大小有限，递归调用次数过多会导致栈溢出
#解决方法是，通过尾递归优化

#尾递归：函数return时调用自身，并且return语句不包含表达式
#sample

def multi_inter(n,product):
	if n==1:
		return product
	else:
		return multi_inter(n-1,n*product)
def multi(n):
	return multi_inter(n,1)
a=multi(5)
print(a)
#尾递归和循环等价，然而python标准解释器没有针对尾递归的优化，==总是存在溢出问题，真棒

def move(n,a,b,c):
	if n==1:
		print('move',a,'--->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(5,'A','B','C')






