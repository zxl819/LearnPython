class Solution:
    def moveZeroes(self, nums: list[int]):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 :
                nums[slow] = nums[fast]
                slow += 1

        
        return nums

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)