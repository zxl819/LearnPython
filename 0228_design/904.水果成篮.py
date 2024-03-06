#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        classFruit = defaultdict(int) #需要提前定义变量类型
        classCount = 0
        i, j = 0, 0
        res = 0
        for i in range(len(fruits)):
            classFruit[fruits[i]] += 1
            if classFruit[fruits[i]] == 1:
                classCount += 1
            while classCount > 2:
                classFruit[fruits[j]] -= 1
                if classFruit[fruits[j]] == 0:
                    classCount -= 1
                j += 1

                
            res = max(i - j + 1, res)
        return res




# @lc code=end

