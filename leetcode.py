res = []
i = 0
nums = [5, 7, 7, 8, 8, 10]
target = 8
        
for i in range(0,len(nums)):
    if nums[i] == target:
        res.append(i)
        print(res)
l = len(res)

if not res:
	print([-1,-1]) 
elif l == 1:
    res.append(res[0])
    print(res)
else:
    res[0],res[1] = res[0],res[-1]
    print(res[:2])

