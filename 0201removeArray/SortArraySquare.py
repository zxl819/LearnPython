import numpy as np
class Solution:
    def sortArraySquare(self, nums: list[int]):
        new = []
        for i in nums:
            new.append(i * i)
        
        new.sort()
        return new
    
    def sortArraySquare2(self, nums: list[int]):
        # 由于最大值在两侧：
        new = [float("inf")] * len(nums)
        l, r = 0 ,len(nums) - 1
        r1 = len(nums) - 1
        while (l <= r):
            if nums[l] ** 2 <= nums[r] ** 2:
                new[r1] = nums[r] ** 2
                r -= 1
                r1 -= 1
            else:
                new[r1] = nums[l] ** 2
                l += 1
                r1 -= 1
                
        return new
    
nums = [-4,-1,0,3,10]
print(Solution().sortArraySquare2(nums))
print(nums)


        