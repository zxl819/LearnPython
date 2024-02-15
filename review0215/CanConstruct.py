class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        from collections import defaultdict
        s_Cnt = defaultdict(int)
        for s in ransomNote:
            s_Cnt[s] += 1
        for x in magazine:
            s_Cnt[x] -= 1
        
        for i in s_Cnt:
            if s_Cnt[i] > 0:
                return False
        return True
ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))