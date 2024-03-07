class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        if sum(nums) < target:
            return 0
        if target in nums:
            return 1
        
        summary = 0
        j = 0
        res = float("inf")
        for i in range(len(nums)):
            summary += nums[i]
            while summary >= target:
                summary -= nums[j]
                res = min(res, i - j + 1)
                j += 1
        return res
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))            
