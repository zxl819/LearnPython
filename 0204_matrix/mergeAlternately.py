class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        res = []
        loop = min(len(word1), len(word2))
        for i in range(loop):
            res.append(word1[i])
            res.append(word2[i])
        if len(word2) > loop:
            res.append(word2[loop:])
        elif len(word1) > loop:
            res.append(word1[loop:])
        return "".join(res)
    
    def mergeAlternately2(self, word1: str, word2: str):
        m, n = len(word1), len(word2)
        i, j = 0, 0

        ans = list()
        while i < m or j < n:
            if i < m:
                ans.append(word1[i])
                i += 1
            if j < n:
                ans.append(word2[j])
                j += 1
        return "".join(ans)


word1 = "ab"
word2 = "pqrs"

print(Solution().mergeAlternately2(word1, word2))