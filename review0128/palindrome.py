class Solution:
    def longestPalindrome(self,s:list[str]):

        res = ""
        
        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if len(res)<len(tmp):
                res = tmp
                
            tmp = self.helper(s,i,i+1)
            if len(res)<len(tmp):
                res = tmp
        return res



    def helper(self,s,l,r):
        while l>= 0 and r< len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    

s = "babad"
print(Solution().longestPalindrome(s))