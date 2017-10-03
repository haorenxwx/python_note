python_notes10_错误

1,'try...except...finally...'
如果认为某段代码出错，可以在try中执行。
如果出错，则直接跳转到except语句块
执行完except语句以后，如果有finally语句块则执行finally
例：
try:
	print('try...')
	s=10/int('a')
	r=10/0
	print('result:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
except ValueError as e:
	print('ValueError', e)
finally:
	print('finally...')
print('END')
可以用不同的except语句来捕获不同的错误
但是只能发现第一个错误

python的错误也是class，所有错误类型继承于BaseException
使用exception时需要注意，它不仅捕获该类型的错误，还把子类一网打尽
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
UnicodeError属于ValueError的子类，不会显示UnicodeError的错误
try...except...还可以跨越多层调用，
def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error: ',e)
bar或foo出现的错误，都可以在main中捕获并处理


2，调用堆栈

# err.py:
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
运行结果：
Traceback (most recent call last):#表示这是错误的跟踪信息
  File "error test.py", line 11, in <module>
    main()#表示调用main的时候出错了，但是原因是第9行
  File "error test.py", line 9, in main
    bar('0')#调用bar的时候出错了，原因在第6行
  File "error test.py", line 6, in bar
    return foo(s) * 2
  File "error test.py", line 3, in foo
    return 10 / int(s)#发现了错误产生的源头，打印如下
ZeroDivisionError: division by zero

3，记录错误
用内置模块logging记录错误信息，程序出错后把错误打印出来，分析原因，同时程序继续运行
# err_logging.py
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
logging可以通过配置，把错误记到日志文件中

4，抛出错误
# err_raise.py
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)#抛出错误
    return 10 / n
foo('0')
常用，捕获一个错误，打印出来的同时，抛出一个错误
def foo(s):
	n=int(s)
	if n==0:
		raise ValueError('invalid value %s' % s)
	return 10/n
def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError')
		raise 
		#raise 不带语句，就可以把错误原样抛出
bar()






