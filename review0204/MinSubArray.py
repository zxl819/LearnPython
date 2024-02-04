class Solution:
    def minSubArray(self, target: int, nums: list[int]):
        i, j = 0, 0
        res = 0
        ans = []


        for j in range(len(nums)):
            res += nums[j]

            while res >= target:
                if not ans or len(ans) > j - i + 1:
                    ans = nums[i: j + 1]
                res -= nums[i]
                i += 1
        return ans
            
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArray(target, nums))