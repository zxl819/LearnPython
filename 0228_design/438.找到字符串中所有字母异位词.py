#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s or not p:
            return None
        n = len(p)
        res = []
        for slow in range(len(s)):
            fast = slow + n
            if self.Anagrams(s[slow:fast], p):
                res.append(slow)
        return res



    def Anagrams(self, p0: str, p1: str):
        checkp0 = Counter(p0)
        checkp1 = Counter(p1)
        if checkp0 == checkp1:
            return True
        else:
            return False

s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))

# @lc code=end

