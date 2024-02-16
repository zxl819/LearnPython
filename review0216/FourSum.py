class Solution:
    def fourSum(self, nums: list[int], target:int):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i>0  and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while (l < r and nums[l] == nums[l+1]):
                            l += 1
                        while (l < r and nums[r] == nums[r-1]):
                            r -= 1
                        l += 1
                        r -= 1
                    
        return res
nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums, target))