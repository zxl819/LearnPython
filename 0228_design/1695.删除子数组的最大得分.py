#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        from collections import Counter
        s = 0
        subArray = Counter()
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in subArray:
                subArray[nums[l]] -= 1
                if subArray[nums[l]] == 0:
                    del subArray[nums[l]]
                s -= nums[l]
                l += 1
            subArray[nums[r]] += 1
            s += nums[r]
            res = max(res, s)
        return res
nums = [4,2,4,5,6]   
print(Solution().maximumUniqueSubarray(nums))      
# @lc code=end

