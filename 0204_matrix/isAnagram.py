from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        needMap = defaultdict(int)
        needCount = 0
        if len(t) != len(s):
            return False

        for i in range(len(s)):
            needMap[s[i]] += 1
            if needMap[s[i]] == 1:
                needCount += 1
        
        for i in range(len(t)):
            needMap[t[i]] -= 1
            if needMap[t[i]] == 0:
                needCount -= 1
            
            if needCount == 0:
                return True
            
        return False



s = "a"
t = "ab"
print(Solution().isAnagram(s, t))