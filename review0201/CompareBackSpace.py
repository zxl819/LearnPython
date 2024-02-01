class Solution:
    def compareBackSpace(self, s: str, t:str):
        s1 = self.helper(s)
        s2 = self.helper(t)
        return s1 == s2

    
    def helper(self, s):
        s0 = []
        for word in s:
            if word != "#":
                s0.append(word)
            elif s0:
                s0.pop()
        return s0
    