class Solution:
    def threeSum(self, nums: list[int]):
        res = []
        nums.sort()
        n = len(nums)
        if n < 3 or not nums:
            return res
        
        for i in range(n):
            if nums[i] > 0 :
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                tol = nums[i] + nums[l] + nums[r]
                if tol > 0:
                    r -= 1
                elif tol < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
        