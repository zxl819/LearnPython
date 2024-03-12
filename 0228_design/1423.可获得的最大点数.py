#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # from collections import deque
        # cardPoints2 = deque()
        # for i in cardPoints:
        #     cardPoints2.append(i)
        # res = 0
        # if len(cardPoints) <= k:
        #     return sum(cardPoints)
        # while k > 0:
        #     res += max(cardPoints2[0], cardPoints2[-1])
        #     if cardPoints2[0] > cardPoints2[-1]:
        #         cardPoints2.popleft()
        #     else:
        #         cardPoints2.pop()
        #     k -= 1
        # return res
        res = float("inf")
        if len(cardPoints) <= k:
            return sum(cardPoints)
        winLen = len(cardPoints) - k
        cur = 0
        for i in range(len(cardPoints)):
            cur += cardPoints[i]
            if i >= winLen -1:
                res = min(cur, res)
                cur -= cardPoints[i - winLen + 1]
        return sum(cardPoints) - res
            
cardPoints = [100,40,17,9,73,75]
k = 3
print(Solution().maxScore(cardPoints, k))

# @lc code=end

