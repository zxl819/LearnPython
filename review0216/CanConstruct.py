class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        from collections import defaultdict
        M_Cnt = defaultdict(int)
        for m in magazine:
            M_Cnt[m] += 1
        
        for r in ransomNote:
            if r not in M_Cnt:
                return False
            else:
                M_Cnt[r] -= 1
                if M_Cnt[r] == 0:
                    del M_Cnt[r]
        return True
ransomNote = "bb"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))            
        
