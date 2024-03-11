#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums)/min(k, len(nums))
        ave = float("-inf")
        # l, r = 0, k - 1
        # while r < len(nums):
        #     subSum = sum(nums[l: r + 1])/k
        #     ave = max(subSum, ave)
        #     l += 1
        #     r += 1
        # return ave
        # sums = 0
        # for i, num in enumerate(nums):
        #     sums += num
        #     if i >= k:
        #         sums -= nums[i - k]
        #     if i >= k - 1:
        #         ave = max(ave, sums)
        # return ave / float(k)
        l=0
        cur=sum(nums[:k])
        ans=cur/k
        for r in range(k,len(nums)):
            cur+=nums[r]
            cur-=nums[l]
            ans=max(ans,cur/k)
            l+=1
        return ans

nums = [0,1,1,3,3]
k = 4
print(Solution().findMaxAverage(nums, k))
# @lc code=end

