class Solution:
    def reverseStr(self, s: str, k: int):
        l, r = 0 , len(str) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s