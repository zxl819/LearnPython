#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        cusSum = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                cusSum += customers[i]
                customers[i] = 0
        maxNum = 0
        cur = 0
        for i in range(len(customers)):
            cur += customers[i]
            if i >= minutes:
                
                cur -= customers[i - minutes]
            maxNum = max(maxNum, cur)    
        return cusSum + maxNum
                

# @lc code=end

