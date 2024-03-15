#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if not s:
            return ""
        OneNum = 0
        for i in s:
            if i == "1":
                OneNum += 1
        tmp = OneNum
        res = ""
        n = len(s)
        while OneNum > 1:
            res += "1"
            OneNum -= 1
        for j in range(n - tmp):
            res += "0"
        res += "1"
        return res

s = "010"
print(Solution().maximumOddBinaryNumber(s))
# @lc code=end

