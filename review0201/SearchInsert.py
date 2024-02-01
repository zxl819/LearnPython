class Solution:
    def searchInsert(self, nums: list[int], target: int):
        l, r = 0, len(nums)-1
        while (l <= r):
            mid  = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        
        return l

nums = [1,3,5,6]
target = 7
Solution().searchInsert(nums, target)