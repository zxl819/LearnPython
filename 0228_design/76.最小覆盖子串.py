#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        needmap = defaultdict(int)
        needCount = 0
        for i in range(len(t)):
            needmap[t[i]] += 1
            if needmap[t[i]] == 1:
                needCount += 1
        
        l = 0
        res = []
        minLen = float("inf")
        for r in range(len(s)):
            needmap[s[r]] -= 1
            if needmap[s[r]] == 0 :
                needCount -= 1
            
            while needCount == 0:
                if minLen >= r - l + 1:
                    res = s[l:r + 1]
                    minLen = min(minLen, len(res))
                needmap[s[l]] += 1
                if needmap[s[l]] > 0:
                    needCount += 1
                l += 1
        return "".join(res)

s = "a"
t = "aa"
print(Solution().minWindow(s, t))                



# @lc code=end

