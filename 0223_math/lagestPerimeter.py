class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse= True)
    
        n = len(nums)
        res = 0
        i = 0
        while (i + 2) < n:
            if nums[i + 2] + nums[i + 1] > nums[i]:
                res += nums[i + 2] + nums[i + 1] + nums[i]
                break
            else: 
                i += 1
        if res != 0:
            return res
        else:
            return 0    

nums = [1,2,1,10]
print(Solution().largestPerimeter(nums))