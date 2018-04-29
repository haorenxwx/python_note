#81.py

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
        	return False
        if nums[0] == nums[-1]:
        	for i in range(len(nums)-1):
        		if nums[i]!=nums[i+1]:
        			nums = nums[i+1:]
        			break
        print(nums)	
        start = 0
        end = len(nums)-1        	
        while start <= end:
            
            mid = (start+end)/2
            if nums[mid] == target:
            	return True
            if nums[start] <= nums[mid]:
            	if nums[start]<=target<=nums[mid]:
            		end = mid-1
            	else:
            		start = mid+1
            else:
            	if nums[mid]<= target <= nums[end]:
            		start = mid+1
            	else:
            		end = mid-1
        return False




if __name__ == "__main__":
	nums = [1,0,1,1,1]
	target = 0
	print Solution().search(nums,target)
