#task_worker.py
import time, sys, queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager:
class QueueManager(BaseManager):
	pass
#通过QueueManager从网络上获取Queue,---注册时值提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器，也就是运行task_master.py的机器
server_addr = '127.0.0.1'
#127.0.0.1通常分配给loopback接口，loopback是一个特殊的网络接口（可以理解为虚拟网卡）
#用于本集中各个应用法之间的网络交互，只要操作系统的网络组件正常，loopback就能工作。
#localhost是一个域名，可以被分配为任意的IP地址，通常情况下指向127.0.0.1（ipv4）和【：：1】（ipv6）

print('Connect to server %s...' %server_addr)
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
#获取Queue的对象
task = m.get_task_queue()
result= m.get_result_queue()
#从task队列取任务，并把结果写在result队列中。
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d ...' %(n,n))
		r = '%d * %d = %d'%(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
print('work exit.')