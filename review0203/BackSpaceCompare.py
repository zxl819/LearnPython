class Solution:
    def backspacecompare(self, s: str, t:str):
        s = self.helper(s)
        t = self.helper(t)
        return s == t

    def helper(self,s):
        s1 = []
        for word in s:
            if word != "#":
                s1.append(word)
            elif s1:
                s1.pop()
        return s1
s = "ab#c"
t = "ad#c"
print(Solution().backspacecompare(s, t))