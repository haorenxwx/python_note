#!/usr/bin/env python3
#-*- coding: utf-8 -*-

' a test module '
__author__='haorenxwx'


#模块 module
#一个.py文件就是一个模块

#为例避免模块名重复，引入‘包’(package)的概念
#按组织目录引入，选一个顶层包名，把模块存入该文件夹下
#	每个包目录下需要包含__init__.py(可以为空，也可以有代码)，否则会被认为是普通文件夹

import sys
#导入sys模块后，我们有sys变量指向该模块，可以访问sys模块的所有功能
def test():
    args = sys.argv
    #sys模块的argv变量，用list储存了命令行所有的参数。 
    #argv至少有一个元素，第一个参数永远是.py文件的名称
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
#python解释器把特殊变量__name__置为__main__,如果在其他地方导入该hello模块
    test()
'''
把上述代码保存在hello.py中，
在命令行中的执行，若为
python hello.py
>>>'hello.py'
python hello.py gakki
>>>'gakki'
'''
#在命令行中执行，python解释器把特殊变量__name__置为__main__
#如果在其他地方导入hello模块时，if判断运行失败


一个模块中，一些变量和函数只嫩在函数内使用，用_xxx或__xxx这样的函数名或变量名表示非公开变量，不应该直接被引用

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

#这里 _private_1,private_2都是private函数变量，方便用来封装和抽象。

python安装第三方模块通常使用pip
