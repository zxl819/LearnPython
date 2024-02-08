class Solution:
    def threeSum(self, nums: list[int]):
        # 去除重复解 对于重复元素：跳过，避免出现重复解
        res = 0
        i, j,  = 0, 0
        ans = []
        while j <= len(nums) - 1:
            for i in range(j + 1, len(nums)):
                res = nums[i] + nums[j]
                for k in range(i + 1, len(nums)):
                    if nums[k] == (0 - res):
                        ans.append([nums[i], nums[j], nums[k]])
            j += 2
        
        return ans

nums = [0,0,0]
print(Solution().threeSum(nums)) 


                    