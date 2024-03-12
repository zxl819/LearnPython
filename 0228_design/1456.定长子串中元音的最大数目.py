#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import deque
        yuanyin = ["a","e","i","o","u"]
        res = deque()
        cnt = 0
        ans = 0
        for i in range(len(s)):
            res.append(s[i])
            if s[i] in yuanyin:
                cnt += 1
            if i >= k - 1:
                ans = max(cnt, ans)
                if s[i - k + 1] in yuanyin:
                    cnt -= 1
                res.popleft()
        return ans
s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))
# @lc code=end

