class Solution:
    def isAnagram(self, s: str, t: str):
        from collections import Counter
        s_Cnt = Counter(s)
        t_Cnt = Counter(t)

        return s_Cnt == t_Cnt