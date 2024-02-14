class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import defaultdict
        s_Cnt, p_Cnt = defaultdict{int}, defaultdict(int)
        for c in p:
            p_Cnt[c] += 1
        
        res = []
        left = 0
        
        for right in range(len(s)):
            s_Cnt[s[right]] += 1

            if right - left + 1 == len(p):
                if s_Cnt == p_Cnt:
                    res.append(left)
                s_Cnt[s[left]] -= 1
                if s_Cnt[s[left]] == 0:
                    del s_Cnt[s[left]]
                left += 1
        return res
