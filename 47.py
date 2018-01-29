#47.py

nums = [1,1,3]
ans = [[]]
for n in nums:
    resans = []
    for l in ans:
        for i in range(len(l)+1):
            resans.append(l[:i]+[n]+l[i:])
            print(resans)
            if i<len(l) and l[i]==n: break
    ans = resans
    #print("l\n")    
    #print(l)
    #print("answer for each n is:")
    print(ans)

print(ans)
