#90subset2.py
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        res = []
        depth = 0
        
        def dfs(start,depth,temp):
        	#temp.sort()
            if temp not in res:
                res.append(temp)
            if depth == len(nums):return
            for i in range(start,len(nums)):
            	temp1 = temp+[nums[i]]
            	temp1.sort()
            	dfs(i+1,depth+1,temp1)
                #dfs(i+1,depth+1,(temp+[nums[i]]))
        
        dfs(0,0,temp)
        return res
a = Solution()
print(a.subsetsWithDup([4,1,4,4]))