from collections import defaultdict
class Solution:
    def minCoverSubarray(self, s:str, t:str):
        needMap = defaultdict(int)
        needCount = 0
        i, j = 0, 0
        res = ""

        for char in t:
            needMap[char] += 1
            if needMap[char] == 1:
                needCount += 1
            
        for j in range(len(s)):
            if s[j] in t:
                needMap[s[j]] -= 1
                if needMap[s[j]] == 0:
                    needCount -= 1
                
            while needCount == 0:
                if not res or len(res) > j - i + 1:
                    res = s[i: j + 1]
                if s[i] in t:
                    needMap[s[i]] += 1
                    if needMap[s[i]] > 0:
                        needCount += 1
                i += 1
        return res

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minCoverSubarray(s, t))
        