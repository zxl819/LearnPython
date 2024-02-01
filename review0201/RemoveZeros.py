class Solution:
    def removeZeros (self, nums: list[int]):
        i = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[i] = nums[fast]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        return nums
    

nums = [0, 1, 0, 3, 12]
print(Solution().removeZeros(nums))
