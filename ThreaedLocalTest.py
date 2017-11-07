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