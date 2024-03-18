#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_cnt = Counter()
        for i in range(len(s1)):
            s1_cnt[s1[i]] += 1
        l = 0
        s2_cnt = Counter()
        for r in range(len(s2)):
            s2_cnt[s2[r]] += 1
            if r - l + 1 == len(s1):
                if s2_cnt == s1_cnt:
                    return True
                s2_cnt[s2[l]] -= 1
                if s2_cnt[s2[l]] == 0:
                    del s2_cnt[s2[l]]
                l += 1
        return False
    

# @lc code=end

