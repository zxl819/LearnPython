class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import defaultdict
        P_Cnt = defaultdict(int)
        for P in p:
            P_Cnt[P] += 1

        left = 0
        res = []
        check = defaultdict(int)
        for right in range(len(s)):
            check[s[right]] += 1
            if right - left + 1 == len(p):
                if check == P_Cnt:
                    res.append(left)
                check[s[left]] -= 1
                if check[s[left]] == 0:
                    del check[s[left]]
                left += 1
        return res

s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))