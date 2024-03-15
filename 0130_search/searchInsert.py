class Solution:
    def searchInsert(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid

nums = [1,3,5,6]
target = 0

print(Solution().searchInsert(nums, target))
    

