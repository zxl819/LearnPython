class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                return i
            else:
                return -1

        

haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))