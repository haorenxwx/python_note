#56.py
nums = [3,2,1,0,4]
#nums = [2,0]
#nums = [2,3,1,1,4]
'''
index = len(nums)-1
def Jump(index, nums):
    #for i in reversed(xrange(len(nums)-1)):
    for i in reversed(xrange(index+1)):
        print(i)
        if index == 0:
            return True

        if nums[index] == -1:
            return False
        for j in xrange(nums[i]):
            if i != index and abs(i-index) == j+1:
                nums[index] = -1
                print(nums)
                return Jump(i,nums)
    return False
print Jump(index,nums)
'''
if len(nums) == 1:
    print True
index,reach = 0,0
while index<len(nums):
    if reach < index:
        print False
    reach = max(reach,nums[index]+index)
    index+=1
print True
