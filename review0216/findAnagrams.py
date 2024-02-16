class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import defaultdict
        P_Cnt = defaultdict(int)
        for P in p:
            P_Cnt[P] += 1

        n = len(p)
        l = 0
        res = []
        checklist = defaultdict(int)

        for r in range(len(s)):
            checklist[s[r]] += 1
            if r - l + 1 == n:
                if checklist == P_Cnt:
                    res.append(l)
                checklist[s[l]] -= 1
                if checklist[s[l]] == 0:
                    del checklist[s[l]]
                l += 1
        return res
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))