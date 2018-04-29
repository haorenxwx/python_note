#639dp.py

import collections
class Solution(object):
    def __init__(self):
        dmap = collections.defaultdict(int)
        ch = '0123456789*'
        for m in ch:
            if m == '*':
                dmap[m] = 9
            elif "1" <= m <= "9":
                dmap[m] = 1
            for n in ch:
                s = m+n
                if m == '*':
                    if n == '*':dmap[s] = 15 #from 10 to 26
                    elif "0" <= n <= "6":dmap[s] = 2
                    else :dmap[s] = 1
                elif m == '1':
                    if n == '*':dmap[s] = 9
                    else: dmap[s] = 1
                elif m == '2':
                    if n == '*':dmap[s] = 6
                    elif '0' <= n <= '6': dmap[s] = 1
        self.dmap = dmap
    def numDecodings(self,s):
        """
        :type s: str
        :rtype: int
        """
        dp1 = dp2 = 1
        ans = 0
        ch = '-'
        mod = 10**9+7
        for c in s:
            ans = (dp1*self.dmap[ch+c]+dp2*self.dmap[c])%mod
            ch = c
            dp1 = dp2
            dp2 = ans
            print('c is: ',c,'ans is: ',ans)
        return ans

if __name__ =="__main__":
	a = Solution()
	print(a.numDecodings('2839')) 



Sleep(2000)




