python_notes11_调试.py
1，logging：推荐用法
不会抛出错误，而是可以输出到文本文件
import logging
logging.basicConfig(filename='logger.log',level=logging.INFO)
#更改Config
#1,指定输出的文件
#2,指定记录信息的级别：debug，info，warning，error

s='0'
n=int(s)
logging.info('n=%d' %n)
print(10/n)


2，print()把有可能的变量打印出来
注意，调试完需要删除

3，assert断言
def foo(s):
	n=int(s)
	assert n!=0,'n is zero'
	return 10/n
def main():
	foo('0')
如果assert后面的语句执行为False，就抛出错误'n is zero'
注意，调试完需要删除，或者启用python解释器-0参数关闭assert
= =不知道为什么并没有抛出错误

4，启动python的调试器pdb
$ python3 -m pdb err.py
进入调试状态，输入'n'表示单步执行代码
输入'p 变量名'查看变量值
输入'q'结束调试

5，pbd.set_trace()不需要单步执行,在可能出错的地方设置一个断电：
#err.py
import pbd

s='0'
n=int(s)
pbd.set_trace()#运行到这里会自动暂停,进入pbd环境，'p'查看变量，'c'继续运行
print(10/n)



