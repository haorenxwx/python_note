#80.py

class Solution:
	def removeDuplicates(self,nums):
		i = 0
		count = 0
		lenth = 1
		print(nums)
		if len(nums)<2:
			print len(nums)
		while i < len(nums)-1:
		            
		    if nums[i] == nums[i+1]:
		        count+=1
		        
		    else:
		        count = 0
		    if count >= 2:
		        lenth -= 1
		        i-=1
		        nums.remove(nums[i])
		    i+=1
		    lenth+=1
		    print("count",count)
		    print('nums',nums)
		print(nums)
		return lenth
		

if __name__ == "__main__":
	print Solution().removeDuplicates([1,1,1,1,2,2,3])