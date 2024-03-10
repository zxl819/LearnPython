#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # slow = 0
        # idx = 0
        # for fast in range(1, len(nums)):
        #     if nums[slow] != nums[fast]:
        #         idx = 0
        #     idx += 1
        #     slow += 1
        #     if idx == 2:
        #         while nums[slow] == nums[fast]:
        #             fast += 1
        #         slow += 1
        #         nums[slow] = nums[fast]
        #         fast += 1
        #         idx = 0

        # slow = 0
        # for i in nums:
        #     if slow < 2 or nums[slow - 2] != i:
        #         nums[slow] = i
        #         slow += 1
        # return slow
        # if len(nums) <= 1:
        #     return len(nums)
        # slow, fast, cnt = 1, 1, 1
        # while fast < len(nums):
        #     if nums[fast - 1] == nums[fast]:
        #         cnt += 1 
        #         if cnt <= 2:
        #             nums[slow] = nums[fast]
        #             slow += 1
        #     else:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #         cnt = 1
        #     fast += 1
        # return slow

        if len(nums) < 2:
            return len(nums)
        slow, fast = 2, 2
        while fast < len(nums):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


nums = [0,0,1,1,1,1,2,3,3]
Solution().removeDuplicates(nums)
# @lc code=end

