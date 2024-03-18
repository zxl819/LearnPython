#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import Counter
        l = 0
        res = []
        P_cnt = Counter()
        S_cnt = Counter()
        for i in p:
            P_cnt[i] += 1
        for r in range(len(s)):
            S_cnt[s[r]] += 1
            if r - l + 1 == len(p):
                if S_cnt == P_cnt:
                    res.append(l)
                S_cnt[s[l]] -= 1
                if S_cnt[s[l]] == 0:
                    del S_cnt[s[l]]
                l += 1
        return res
                    
            
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
# @lc code=end

