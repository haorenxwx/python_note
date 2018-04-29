#93_dfs_restoreIP.py
class Solution(object):
    def restoreIpAddresses(self, s):
        res = ""
        #res = []
        resout = []
        #if len(s)<8 or len(s)>12:
        #    return None
        
        def IPadd(s,length,res,resout):
            print('res',res)
            if length == 4:
                if not s:
                    #resout.append('.'.join(res))
                    resout.append(res[1:])
                    print('resout',resout)
                return
            for a in [1,2,3]:
                if a <= len(s):
                    temp = s[:a]
                    if int(temp)<=255:
                        res.append(temp)
                        IPadd(s[a:],length+1,res+'.'+temp,resout)
                        #IPadd(s[a:],length+1,res,resout)
                        if s[0] == '0':
                            break


        IPadd(s,0,res,resout)
        return resout

if __name__ == '__main__':
    a = Solution()
    s = "25525511135"
    print(a.restoreIpAddresses(s))