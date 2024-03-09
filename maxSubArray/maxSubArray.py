class Solution:
    def maxSubArray(self, nums: list[int]):
        for i, value in enumerate(nums):
            if value == max(nums):
                idx = i
                break
        i = j = idx
        while i > 0 and j < len(nums) - 1:


                
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
Solution().maxSubArray(nums)





