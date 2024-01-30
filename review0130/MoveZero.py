class Solution:
    def moveZeroes(self,nums:list[int]):
        if not nums:
            return 0
        slow = 0
        fast = 0
        while fast <= len(nums)-1:   
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        for i in range(slow,len(nums)):
            nums[i] = 0
        return nums
    
nums = [0]
print(Solution().moveZeroes(nums))
            

