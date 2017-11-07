python_note21分布式进程

thread 和process首选process，process可以分不到多台机器上，thread最多可以分配到一台机器的多个CPU上

multiprocessing模块不但支持多进程，他的managers子模块还支持把多进程分布到多个机器上
例：
有一个通过Queue通信的多进程程序在同一台机器上运行，现在要把发送任务的进程和处理任务的进程分布到两台机器上：

服务进程：
启动Queue，把queue注册到网络上，往Queue里写入任务

#task_master.py
import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseManagement继承的QueueManager:
class QueueManager(BaseManager):
	pass

#把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)

#绑定端口5000，设置验证码‘abc’：
manager = QueueManager(address=('',5000), authkey=b'abc')
#启动Queue
manager.start()
#获得通过网络访问的Queue对象：
task = manager.get_task_queue()
task = manager.get_result_queue()
#放几个任务进去：
for i in range(10):
	n = random.randint(0,10000)
	print('Put task %d ...' %n)
	task.put(n)
#从result队列读取结果
print('Try get results...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)
#关闭
manager.shutdown()
print('master exit')

在一台机器写多进程程序是，创建的queue可以直接使用
但是在分布式多进程环境下添加到Queue不能对原始task_queue操作,这样就绕过了QueueManger的封装
需要通过manager.get_task_queue()获得Queue 添加接口

在另一台机器上写多进程程序（本机也可以使用）：
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

启动task_master.py的服务进程
运行结果如下：
$ python task_master.py 
Put task 3411...
Put task 1605...
Put task 1398...
Put task 4729...
Put task 5300...
Put task 7471...
Put task 68...
Put task 4219...
Put task 339...
Put task 7866...
Try get results...

task_master.py进程发送完任务后，等待result队列的结果。
启动task_worker.py进程

$ python task_worker.py
Connect to server 127.0.0.1...
run task 3411 * 3411...
run task 1605 * 1605...
run task 1398 * 1398...
run task 4729 * 4729...
run task 5300 * 5300...
run task 7471 * 7471...
run task 68 * 68...
run task 4219 * 4219...
run task 339 * 339...
run task 7866 * 7866...
worker exit.

task_worker.py进程结束以后，在task_master.py进程中继续打印结果
Result: 3411 * 3411 = 11634921
Result: 1605 * 1605 = 2576025
Result: 1398 * 1398 = 1954404
Result: 4729 * 4729 = 22363441
Result: 5300 * 5300 = 28090000
Result: 7471 * 7471 = 55815841
Result: 68 * 68 = 4624
Result: 4219 * 4219 = 17799961
Result: 339 * 339 = 114921
Result: 7866 * 7866 = 61873956

如果把n*n代码换成发送邮件，就实现了邮件队列的异步发送。
Queue储存在task_master.py进程中

Queue之所以能访问网络，就是通过QueueManager实现的。因为QueueManager管理的不止一个Queue
所以要给每一个Queue的网络调用接口起名字:get_task_queue

