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
    #
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()