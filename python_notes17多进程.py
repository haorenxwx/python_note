python_notes17多进程multiprocessing.py

多任务：操作系统同时运行多个任务(单核/多核)
并行执行多任务：在多核CPU上执行，每个cpu执行多个任务(时间交替)

进程(Process)：对于一个系统来说，一个任务就是一个进程
线程(Thread)：在一个进程内部的子任务(最小的执行单元)

多任务的解决方案：
1：启动多进程，每个进程对应一个线程
2：一个进程，在进程内启动多个子进程
3：多进程+多线程


多进程multiprocessing：
Unix/Linux 系统提供了fork()函数（****windows不能用****mac基于BSD，可以），调用一次返回两次：
	系统吧当前进程（父进程）复制了一份（子进程），分别在父进程和子进程里返回
	父进程返回子进程ID，子进程返回0
	（父进程要记下每个子进程的ID，子进程调用 getppid()拿到父进程ID）
import os
print('Process (%s) start...' % os.getpid())
pid=os.fork()
if pid == 0:
	print('I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid()))
else:
	print('I (%s) just created a child process (%s).' %(os.getpid(),pid))

multiprocessing模块--跨平台多进程

from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' %(name,os.getpid()))
if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p=Process(target=run_proc,args=('test',))#传入执行函数和执行参数
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')


Pool
启动大量子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...'%(name, os.getpid()))
	start = time.time()#得到当时的时间戳
	time.sleep(random.ramdom() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__=='__main__':
	print('Parent process %s.' %os.getppid())
	p=Pool(4)#表示最多同时执行4个进程，
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocess done...')
	p.close()
	p.join()#调用join()方法，等待所有子进程执行完毕，
	#调用join之前必须先调用close(),调用close()之后，就不能添加新的process了

	print('All subprocess done.')


Subprocess
用子进程，调用一个外部进程，控制子程序的输入和输出

import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('Exit code: ', r)

子进程如果还需要输入，可以用communication()方法输入
import subprocess
print('$ nslookup')
p=subprocess.Popen(['nslookup'],sdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communication(b'set q=mx\npython.org\nexit\n')
#相当于在执行命令nslookup之后，手动输入：
#q=mx 
#python.org 
#exit
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


