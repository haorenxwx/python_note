#46.py



'''
if not nums:
    print(nums)
resout = []
nums.sort()
partition = -1

j = 0
number = reduce(lambda x,y:x*y,range(1,len(nums)+1))
resout = [""]*(number+1)
while j<= number:
    i = len(nums)-1
    resout[j] = list(nums)
    while i>0:
        if nums[i-1]<nums[i]:
            partition = i-1
            break
        i-=1
    for i in xrange(len(nums)-1,-1,-1):
        if nums[i]>nums[partition]:
            nums[i],nums[partition] = nums[partition],nums[i]
            nums[partition+1:] = sorted(nums[partition+1:])
        #elif nums[i]<nums[partition] and i == 0:
            #nums[partition:] = sorted(nums[partition:])
    print(partition)
    print(nums)
    #resout.append(nums)
     
    j+=1
    print(resout)
    print("\n")
print(resout)
'''

def per(self,nums):
	return [[n]+p 
		for i,n in enumerate(nums)#start from i...
		for p in self.permute(nums[:i]+nums[i+1:])] or [[]]



