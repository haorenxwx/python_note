python_notes19ThreadLocal.py

ThreadLocal
多线程环境下，每个线程都有自己的数据，一个线程使用自己的局部变量比使用全局变量好
局部变量只能自己看到，不会影响其他线程

全局变量修改必须加锁

1，局部变量调用
但是局部变量函数调用时，传递比较麻烦：
def process_student(name):
	std = Student(name)
	do_task_1(std)#std虽然是局部变量，但是每个函数都要使用，所以要传下去
	do_task_2(std)
def do_task_1(std):
	do_subtask_1(std)
	do_subtask_2(std)
......

2，用全局dict存放Student对象，然后thread作为key获得对应Student对象
global_dict = {}
def std_thread(name):
	std = Student(name)
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()
def do_task_1():
	#不传入std，根据当前线程查找
	std = global_dict[threading.current_thread()]
	...
def do_task_2():
	std = global_dict[threading.current_thread()]
	...

3, TreadLocal,不用查找dict，自动完成
import threading
#创建全局ThreadLocal对象
local_school = threading.local()

def process_age():
	another = local_school.age
	print('In another situation, age is %s'%(another))
def process_student():
	std = local_school.student
	std2 = local_school.age
	print('Hello, %s(in %s) is in age of %s'%(std, threading.current_thread().name, std2))
def process_thread(name,age):
	local_school.student = name
	local_school.age = age
	process_student()
	process_age()

t1 = threading.Thread(target = process_thread, args=('Alice','18',),name='Thread-A')
t2 = threading.Thread(target = process_thread, args=('Bob','20',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

local_school是ThreadLocal的对象，每一个thread都可以读写student的属性，并且互不影响
可以理解全局变量local_school是一个dict， 不但可以用local_school.student, 还可以绑定其他的变量：local_school.teacher

ThreadLocal 常用的地方就是为每个线程绑定一个数据库链接，http请求，用户身份信息，
这样一个线程所有调用的处理函数都可以非常方便的访问这些资源
----------------解决了一个线程中，个函数之间互相传递的问题。