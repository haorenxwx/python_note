#77.py

#low efficient......
n = 5
k = 3
'''
k1 = k
res = []
num = []
temp = []
for i in range(1,n+1):
    num.append(i)

def comb(num,k,temp,res):
    if k == 0:
        
    	#if sorted(temp)!= temp:
    	#	return res
    	#else:
    	#	return res.append(temp)####
        
        return res.append(temp)

    for i in xrange(len(num)-k+1):
        if temp != []:
        	if num[i]>temp[-1]:
        		comb(num[:i]+num[i+1:],k-1, temp+[num[i]],res)
        else:
        	comb(num[:i]+num[i+1:],k-1, temp+[num[i]],res)    
comb(num,k,temp,res)
print(res)
'''
temp = []
res = []
x = 1
while True:
    l = len(temp)
    print('n-k+l+1',n-k+l+1)
    if l == k:
        res.append(temp[:])
    if l == k or x>n-k+l+1:
        if not temp:
            print('result',res)
            break
        print('pop',temp,'x value',x)
        x = temp.pop()+1
        
    else:
    	print('append',temp,'x value',x)
        temp.append(x)
        
        x+=1




