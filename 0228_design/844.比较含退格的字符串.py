#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not s or not t:
            return True
        return self.backspace(s) == self.backspace(t)
    
    def backspace(self, s:str):
        stackS = []
        for i in range(len(s)):
            cur = s[i]
            if s[i] == "#":
                if stackS:
                    stackS.pop()
                i += 1
            else:
                stackS.append(cur)

        return stackS
s = "ab##"
t = "c#b#"
print(Solution().backspaceCompare(s, t))

# @lc code=end

