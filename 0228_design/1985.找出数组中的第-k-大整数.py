#
# @lc app=leetcode.cn id=1985 lang=python3
#
# [1985] 找出数组中的第 K 大整数
#

# @lc code=start
class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        n = len(nums)
        target = n - k
        left = 0
        right = n - 1
    
    def paritition(self,nums: list[str], left: int, right: int):
# @lc code=end

