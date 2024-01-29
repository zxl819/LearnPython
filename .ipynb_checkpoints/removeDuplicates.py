class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0

        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        return nums

    
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        fast = 0

        while fast <= len(nums)-1:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        
        for j in range(slow,len(nums)):
            nums[j] = 0
        return nums
nums = [0,0,1,1,1,2,2,3,3,4]



print(Solution().removeDuplicates(nums))
#print(Solution().moveZeroes(nums))