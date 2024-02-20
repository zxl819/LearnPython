class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = self.Duplicates(s)
        while self.check(res):
            res = self.Duplicates(res)
        return res



    def check(self, s: str):
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                return True
        return False

    def Duplicates(self, s: str):
        slow = 0
        fast = 1
        res = []
        while fast <= len(s) - 1:
            if s[fast] != s[slow]:
                res.append(s[slow])
                slow += 1
                fast += 1
            else:
                fast += 2
                slow += 2
        if slow < len(s):
            res.append(s[len(s)-1])
        res.append(s[len(s)-1])
        return res
    
    def removeDuplicates2(self, s:str):
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
s = "abbaca"
print(Solution().removeDuplicates(s))