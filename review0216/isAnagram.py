class Solution:
    def isAnagram(self, s: str, t: str):
        from collections import Counter
        S_Cnt = Counter(s)
        T_Cnt = Counter(t)
        return S_Cnt == T_Cnt