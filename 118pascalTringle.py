#118pascalTringle.py

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        
        res.append([1])
        self.dfs(numRows,res)
        return res
        
    def dfs(self,numRows,res):
        if numRows == 1:
            return [1]
        temp = self.dfs(numRows-1,res)
        print(temp)
        temp1 = []
        for i in range(len(temp)):
            if i == 0 :
                temp1 = temp1+[1]
            else:
                temp1 = temp1+[temp[i-1]+temp[i]]
        temp1 = temp1+[1]
        print('temp',temp)
        print(temp1)
        res.append(temp1)
        return temp1
if __name__ == '__main__':
    a = Solution()
    res = a.generate(5)
    print(res)
