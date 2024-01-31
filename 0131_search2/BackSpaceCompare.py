class Solution:
    def backSpaceCompare(self, s: str, t: str):
        s1 = self.helper(s)
        s2 = self.helper(t)
        return bool(s1 == s2)

    def helper(self, s):
        s1 = []
        for fast in range(len(s)):
            if s[fast] != "#":
                s1.append(s[fast])
            else:
                s1.pop()
        return "".join(s1)

s = "ab##"
t = "c#d#"
print(Solution().backSpaceCompare(s, t))



            
