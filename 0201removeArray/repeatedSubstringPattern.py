from collections import defaultdict
class Solution:
    def repeatedSubstringPattern(self, s: str):
        pattern = []
        check = []
        while i < len(s) - 1:
            pattern.append(s[i])
            if s[i + 1] == pattern[0]:
                j = i + 1
                while j < len(pattern):
                    check.append(s[j])
                    j += 1
            i += 1
                                     
