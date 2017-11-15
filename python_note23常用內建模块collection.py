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
	q.append('x')
	q.appendleft('y')

defaultdict
- 使用dict时，如果引用的Key不存在，会抛出Keyerror
	如果希望在key不存在时返回一个默认值，就可以使用defaultdict
	from collections import defaultdict
	dd = defaultdict(lambda: 'N/A')
	dd['key1'] = 'abc'
	dd['key2'] # do not exit, return N/A
- 除了不返回默认值 defaultdict在其他行为和dict是完全一样的

OrderedDict
- 使用dict时，key是无序的，所以对dict做迭代的时候，无法确认key的顺序。
- OrderedDict 按照插入的顺序排序
	from collections import OrderedDict
	od = OrderedDict()
	od['z'] = 1
	od['y'] = 2
	od['x'] = 3
	list(od.keys())

OrderedDict可以实现FIFO（先进先出）的dict当容量超出限制，先删除最早添加的key
	from collections import OrderedDict
	class LastUpdatedOrderedDict(OrderedDict):
    	def __init__(self, capacity):
        	super(LastUpdatedOrderedDict, self).__init__()
        	self._capacity = capacity

    	def __setitem__(self, key, value):
        	containsKey = 1 if key in self else 0
        	if len(self) - containsKey >= self._capacity:
            	last = self.popitem(last=False)
            	#popitem() is useful to destructively iterate over a dictionay
            	#popitem(last=False) 移除dict中第一组元素
            	#popitem(last=True) 移除dict中最后一组元素
            	print('remove:', last)
        	if containsKey:
            	del self[key]
            	print('set:', (key, value))
        	else:
            	print('add:', (key, value))
        	OrderedDict.__setitem__(self, key, value)

Counter
一个简单的计数器，统计字符出现的个数
	from collections import Counter
	c = Counter()
	for ch in 'programming':
		c[ch] = c[ch] + 1
		
