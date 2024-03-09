class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        i, j = 0, 0
        summary = 0
        cnt = 0
        for i in range(len(nums)):
            summary += nums[i]
            if summary == k:
                cnt += 1
            while summary != k:
                summary -= nums[j]
                j += 1
        return cnt
nums = [-1,-1,1]
k = 3
print(Solution().subarraySum(nums, k))    

