class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        from collections import defaultdict
        r_dict = defaultdict(int)
        for r in ransomNote:
            r_dict[r] += 1
        for m in magazine:
            r_dict[m] -= 1
        for x in r_dict:
            if r_dict[x] > 0:
                return False
        
        return True
    

ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine))
