#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        cnter = Counter()
        l, r = 0, 0
        while r < len(s):
            while s[r] in cnter:
                cnter[s[l]] -= 1
                if cnter[s[l]] == 0:
                    del cnter[s[l]]
                l += 1
            cnter[s[r]] += 1
            res = max(res, r - l + 1)
            r += 1
        return res
s = "au"
print(Solution().lengthOfLongestSubstring(s))

# @lc code=end

