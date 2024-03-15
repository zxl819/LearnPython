from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        needMap = defaultdict(int)
        needCount = 0
        for i in range(len(s)):
            needMap[s[i]] += 1
            if needMap[s[i]] == 1:
                needCount += 1
        for i in range(len(t)):
            needMap[t[i]] -= 1
            if needMap == 0:
                needCount -= 1
            if needMap[t[i]] < 0:
                return t[i]



s = "a"
t = "aa"
print(Solution().findTheDifference(s, t))