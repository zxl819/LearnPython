#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        s = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            s += nums[r]
            while s - nums[l] >= target:
                s -= nums[l]
                l += 1
            if s >= target:
                res = min(res, r - l + 1)
        return res if res <= len(nums) else 0
target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))
# @lc code=end

