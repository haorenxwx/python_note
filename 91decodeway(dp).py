#91decodeway(dp).py

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        df = [1,1]
        if s == "" or s[0] == "0": return 0
        for i in range(2,len(s)+1):
            if 10<=int(s[i-2:i])<=26 and s[i-1]!='0':
                df.append(df[i-1]+df[i-2])
            elif int(s[i-2:i]) == 20 or int(s[i-2:i]) == 10:
                df.append(df[i-2])
            elif s[i-1]!='0':
                df.append(df[i-1])
            else:
                return 0
        #return df[len(s)]
        return df[-1]
a = Solution()
print(a.numDecodings("10"))
