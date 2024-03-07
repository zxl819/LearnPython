from collections import defaultdict
class Solution:
    def minWindoe(self, s:str, t:str):
        needMap = defaultdict(int)
        needCount = 0
        i, j = 0, 0
        res = ""

        for ch in t:
            needMap[ch] += 1
            if needMap[ch] == 1:
                needCount += 1
        
        for i in range(len(s)):
            if i in t:
                needMap[s[i]] -= 1
                if needMap[s[i]] == 0:
                    needCount -= 1
            
            while needCount <= 0:
                if not res or len(res) > i - j + 1:
                    res = [i: j + 1]


                if s[j] in t:
                    needMap[s[j]] += 1
                    if needCount > 0:
                        needCount += 1
                j += 1
            

        return res
