class Solution:
    def RemoveZero(self, nums: list[int]):
        if not nums:
            return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!= 0:
                nums[slow] = nums[fast]
                slow += 1
        
        for i in range(slow, len(nums)):
            nums[i] = 0

        return nums
    
nums = [0,1,0,3,12]
print(Solution().RemoveZero(nums))