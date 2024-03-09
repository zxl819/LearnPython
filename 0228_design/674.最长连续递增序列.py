#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        n = len(nums)
        res = 0
        while (fast < n):
            if (fast > 0 and nums[fast - 1] >= nums[fast]):
                slow = fast
            res = max(res, fast - slow + 1)
            fast += 1
        return res
        

nums = [1,3,5,4,7]
print(Solution().findLengthOfLCIS(nums))
# @lc code=end

