#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        zero = 0
        two = len(nums)
        i = 0
        while i < two:
            if nums[i] == 0:
                self.swap(nums, i, zero)
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                self.swap(nums, i, two)

    def swap(self, nums: list[int], idx1: int, idx2: int):
        tmp = 0
        tmp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = tmp
        # return nums[idx1], nums[idx2]

# @lc code=end

