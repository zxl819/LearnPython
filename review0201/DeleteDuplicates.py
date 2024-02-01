class Solution:
    def deleteDuplicates (self, nums: list[int]):
        slow = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            
        return slow + 1
            