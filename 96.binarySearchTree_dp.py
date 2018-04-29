#96.binarySearchTree_dp.py

class Solution(object):
    def numTrees(self, s):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1,2]
        if s <= 2:
            return dp[s]
        else:
            dp += [1 for i in range(s-2)]
            print(dp)
            for i in range(3,s+1):
                for j in range(1,i+1):
                    dp[i] += dp[j-1]*dp[i-j]
            print(dp)
            return dp[s]
if __name__ == '__main__':
    a = Solution()
    print(a.numTrees(4))