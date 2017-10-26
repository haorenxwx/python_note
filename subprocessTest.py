from multiprocessing import Process,Queue
import os, time, random

def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
#读数据进程的执行代码
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue' % value)
if __name__=='__main__':
	q=Queue()#父进程创建Queue，并传给各个子进程
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()#启动子进程pw，写入
	pr.start()#启动子进程pr，读取

	pw.join()
	pr.terminate()