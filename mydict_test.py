#mydict_test.py
import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
	def setUp(self):
		print('setup...')
	def tearDown(self):
		print('tearDown...')
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