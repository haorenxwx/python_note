#119map.py
class Solution(object):
	def getRow(self, rowIndex):
		res = [1]
		for i in range(rowIndex):
			res = map(lambda x,y: x+y, res+[0],[0]+res)
		return res
if __name__ == '__main__':
	a = Solution()
	print(a.getRow(1))	