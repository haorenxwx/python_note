# python_notes18多线程.py

多任务，可以由多进程完成，也可以由一个进程的多个线程完成
python 线程是真的posix thread，而不是模拟出来的线程

python标准库提供两个模块：_thread 和 threading. threading 模块对_thread进行了封装

启动线程，把一个函数传入并创建Thread实例，调用start()开始执行

import time, threading
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	#current_thread,返回当前线程的实例
	n = 0
	while n < 5:
		n=n+1
		print('thread %s >>> %s' %(threading.current_thread().name,n)
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
#把函数loop传入threading,并创建实例LoopThread(子线程实例名字，在创建时指定)
#如果不指定名字，就自动命名为Thread-1, Thread-2...
t.start()#此时运行子线程，LoopThread
t.join()
print('thread %s ended' % threading.current_thread().name)
#此时运行主线程MainThread


Lock
多线程和多进程最大的不同在于，
多进程中，各自有一份拷贝存在于每个进程中，
多线程中，所有变量所有线程共享，可能存在多个线程同时修改一个变量的情况

import time, threading 
balance = 0
def change_it(n):
	global balance
	balance = balance+n
	balance = balance-n
def run_thread(n):
	for i in range(10000):
		change_it(n)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

因为两个线程会同时执行时，修改balance时需要多条语句，线程可能中断，导致多个线程把一个对象的内容该改乱
保证计算正确，需要给change_it上锁
同一时间只有一个线程执有该锁：

balance = 0
lock = threading.Lock()

def run_thread(n):
	for i in range(1000):
	#获取锁
	lock.acquire()
	try:
		change_it(n)
	finally:
		lock.release()
		#改完以后一定要释放锁
获得锁的线程用完以后一定要释放锁，否则等待锁的线程会永远等待下去，成为死线程
但是阻止了多线程的并发执行，效率大大下降。 

在python中，因为GIL（Global Interpreter Lock）存在，无法真正利用多核，
