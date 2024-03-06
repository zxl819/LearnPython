#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
# import numpy as np
class Solution:
    def sortedSquares(self, nums: list[int]):
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                res.append(nums[j] ** 2)
                j -= 1
            elif nums[i] ** 2 >= nums[j] ** 2:
                res.append(nums[i] ** 2)
                i += 1
        return res[::-1]
nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))


# @lc code=end

