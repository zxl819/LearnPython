#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        l = 0
        res = 0
        for r in range(len(arr) - 1):
            if r % 2 == 0:
                if arr[r] > arr[r + 1]:
                   r += 1
                elif arr[r] <= arr[r + 1]:
                    l += 1
            elif r % 2 != 0:
                if arr[r] < arr[r + 1]:
                    r += 1
                elif arr[r] >= arr[r + 1]:
                    l += 1
            res = max(res, r - l + 1)
        return res
arr = [9,4,2,10,7,8,8,1,9]
print(4 // 2)
print(Solution().maxTurbulenceSize(arr))
# @lc code=end
print(45 % 64)
