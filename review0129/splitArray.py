class Solution:
    def splitArray(self,nums:list[int]):
        nums.sort()
        return sum(nums[::2])
nums = [6,2,6,5,1,2]
print(Solution().splitArray(nums))