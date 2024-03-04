#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        from collections import defaultdict
        five = ten = 0
        for b in bills:
            if b  == 5:
                five += 1
            elif b == 10:
                five -= 1
                ten += 1
            elif ten:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True


                    



                
# @lc code=end

