class Solution:
    def search(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return right + 1
            

nums = [1,3,5,6]
target = 7


print(Solution().search(nums, target))