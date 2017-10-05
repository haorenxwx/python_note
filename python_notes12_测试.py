python_notes12_测试.py
单元测试：
对一个模块，函数，或一个类，进行正确性检验的工作

首先编写一个dict类,储存在mydict.py中：
class Dict(dict):
	def __init__(self,**kw):#**kw表示支持任意多的参数
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" %key)
	def __setattr__(self,key,value):
		self[key]=value

编写测试单元，储存在mydict_test.py中：
import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)#unittest 中用来测试相等的方法
		self.assertEqual(d.b,'test')#检测值是否一样
		self.assertTrue(isinstance(d,dict))#检测类型是否一样
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):#
			value=d.empty
#运行方式1
if __name__=='main':#可以把mydict_test.py直接当做脚本运行
	unittest.main()
#运行方式2--->推荐，一次可以运行多个单元
python -m unittest mydict_test




在单元测试中编写两个特殊的方法setup(),teardown()
setUp与tearDown两个方法在每一个调用的测试方法前后分别执行，
class TestDict(unittest.TestCase):
	def setUp(self):
		print('setup...')
	def tearDown(self):
		print('tearDown...')
#检验4个class，调用4次
单元测试通过不一定没有bug，不通过肯定要有bug

