from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str):
        i, j = 0, 0
        needMap = defaultdict(int)
        needCnt = len(t)
        res = ''

        for char in t:
            needMap[char] += 1

        while j < len(s):

            if s[j] in needMap:
                if needMap[s[j]] > 0:
                    needCnt -= 1
                needMap[s[j]] -= 1

            while needCnt == 0:
                if not res or j - i + 1 < len(res):
                    res = s[i:j+1]
                
                if s[i] in needMap:
                    if needMap[s[i]] == 0:
                        needCnt += 1
                    needMap[s[i]] += 1
                i += 1

            j += 1
        return res

 



s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s,t))



