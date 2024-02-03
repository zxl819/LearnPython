class Solution:
    def insertPosition(self, nums: list[int], target: int):
        l, r = 0, len(nums) -1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid -1
            elif nums[mid]< target:
                l = mid + 1
            else:
                return mid
        return l

nums = [1,3,5,6]
target = 2

print(Solution().insertPosition(nums, target))