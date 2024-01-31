class Solution:
    def BackSpace (self, s: str, t: str):
        ss = self.helper(s)
        tt = self.helper(t)
        return ss == tt


    def helper (self, s):
        s1 = []
        for i in s :
            if i != "#":
                s1.append(i)
            elif s1:
                s1.pop()
        return s1


s = "ab#c"
t = "ad#c"
print(Solution().BackSpace(s,t))