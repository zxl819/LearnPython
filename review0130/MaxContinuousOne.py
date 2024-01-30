class Solution:
    def MaxContinuousOne(self,nums:list[int]):
        slow  = 0
        Max_length = 0
        for fast in range(len(nums)):
            if nums[fast] == 1:
                slow += 1
                Max_length = max(Max_length,slow)
            else:
                slow = 0
        
        return Max_length
nums = [1,1,0,1,1,1]
print(Solution().MaxContinuousOne(nums))
