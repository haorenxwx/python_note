python_note29常用內建模块contextlib文件管理.py

python中读写文件以后要正确的关闭

try:
	f = open('PATH','r')
	f.read()
finally:
	if f:
		f.close()

可以简化为：
	with open('PATH','r') as f:
		f.read()
对任何对象，只要正确的实现了上下文管理，就可以用于with语句
实现上下文管理是通过，__enter__ 和 __exit__两个方法实现的
class Query(object):
	def __init__(self,name):
		self.name = name
	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')

	def query(self):
		print('Query info about %s...' % self.name)
这样可以把自己写的资源'query'对象用于with语句：
with Query('Bob') as q:
	q.query()

@contextmanager用法
1: enable with 功能
from contextlib import contextmanager
class Query(object):

	def __init__(self, name):
		self.name = name

	def query(self):
		print('Query info about %s...' % self.name)
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
#装饰器contextmanager 接受一个generator，用yield把with...as var输出
#with就可以正常工作了

with create_query('Bob') as q:
	q.query()

2：在某段代码执行前后自动执行特定代码
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
代码执行结果：
<h1>
hello
world
</h1>
执行顺序：
执行yield前的， yield执行，调用with内部所有语句，执行yield之后的语句

@closing用法
对象没有实现上下文的时候，用closing把对象变成上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

closing也是一个经过@contextmanager装饰的geneartor
@contextmanager
def closing(thing):
	try:
		yield thing
	finally:
		thing.close()



