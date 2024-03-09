#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
    
nums = [1,1,2]
Solution().removeDuplicates(nums)

# @lc code=end

