#89graycode.py
class Solution(object):
    def __init__(self):
        #self.base = ["0","1"]
        self.base = [0,1]
        
    def next(self,basecode,label):
        ans = []
        for i in basecode:
            newcode = '%s%s' % (label,i)
            ans.append(newcode)
        if label == 1:
            ans.reverse()
        return ans
        
    def makenext(self):
        makenext1 = self.next(self.base,0)
        makenext2 = self.next(self.base,1)
        res = makenext1+makenext2
        self.base = res
            
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
        	return [0]      
        for i in range(n-1):
            self.makenext()
        
        #return self.base 
        '''
        a = self.base
        for i in range(len(a)):
        	a[i] = int(a[i],2)
        return a
        '''
        a1 = self.base
        return list(map(lambda x: int(x,2),a1))
        
a = Solution()
print(a.grayCode(3))