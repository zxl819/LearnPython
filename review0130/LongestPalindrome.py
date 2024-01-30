class Solution:
    def LongestPalindrome(self,s:list[str]):
        res = []
        for left in range(len(s)):
            tmp = self.helper(s,left,left)
            if len(tmp) > len(res):
                res = tmp

            tmp = self.helper(s,left,left+1)
            if len(tmp) > len(res):
                res = tmp
        return res




    def helper(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
s = "cbbd"
print(Solution().LongestPalindrome(s))