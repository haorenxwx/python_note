python_note23常用內建模块collection.py

collections 是python的集合类，提供了很多集合模块

namedtuple
- tuple表示不变集合
- namedtuple是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
	from collections import namedtuple
	Point = namedtuple('Point', ['x','y'])
	p = Point(1,2)
	p.x#可以根据属性引用
	p.y
如果要用坐标和半径表示一个圆
	#namedtuple('名称'，[属性list])
	Circle = namedtuple('Circle', ['x','y','r'])


deque
- 使用list储存数据时，按索引访问元素很快，但是插入和删除元素就很慢
	因为list是线性储存，数据量大的时候，插入和删除的效率很低
- deque是为了高效实现插入和删除的双向列表，适合队列和栈
	from collections import deque
	q = deque(['a','b'])

