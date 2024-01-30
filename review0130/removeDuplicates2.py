class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
               
        
        return nums
    
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
