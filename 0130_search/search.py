class Solution:
    def search1(self, nums: list[int], target: int): #[left, right]
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
    

    def search2(self, nums: list[int], target: int): #[left, right)
        left, right = 0, len(nums) - 1
        while (left < right):
            mid  = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid 
            else:
                return mid
        return -1



    
nums = [-1,0,3,5,9,12]
target = 9

print(Solution().search2(nums, target))




