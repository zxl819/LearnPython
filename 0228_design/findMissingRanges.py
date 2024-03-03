class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        if not nums:
            return [[lower, upper]]
        res = []        
        i = lower
        while i >= lower and i <= nums[-1]:
            if i not in nums and i > nums[0]:
                idx = nums.index(i - 1)
                res.append([i, nums[idx + 1] - 1])
                i = nums[idx + 1]
            elif i not in nums and i < nums[0]:
                idx = nums.index(nums[0])
                res.append([i, nums[idx] - 1])
                i = nums[idx]
            else:
                i += 1
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        return res
nums = [1,3]
print(Solution().findMissingRanges(nums, 0, 9))

