python_note28常用內建模块itertools操纵迭代对象.py

- itertools提供的无限迭代器：

1：count() 创建一个无限的迭代器
import itertools
naturals = itertools.count(1)
for n in naturals:
	print(n)

2：cycle() 把传入的一个序列无限重复下去
import itertools
cs = itertools.cycle('ABC')
for c in cs:
	print(c)

3: repeat() 把一个元素无线重复下去，提供第二个参数可以限定重复次数
ns = itertools.repeat('A',3)
for n in ns:
	print(n)

4: takewhile()根据条件判断截取一个有限的序列
natural = itertools.count(1)
ns = itertools.takewhile(lambda x: x<= 10,natuals) 

5: chain() 可以把一组迭代对象串联起来，形成更大的迭代对象
for c in itertools.chain('ABC','XYZ'):
	print(c)

6: groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAAABBBBCCCCYYY'):
	print(key, list(group))

如果要忽略大小写分组：
for key, group in itertools.groupby('AaaBBbCCCcc',lambda c: c.lower()):#或者写upper，把key都换成大写
	print(key, list(group))

itertools返回值不是list，都是Iterator，只有在for循环迭代的时候才真正运算。