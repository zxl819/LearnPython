class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        needMap = defaultdict(int)
        needCount = 0
        for s in ransomNote:
            needMap[s] += 1
            if needMap[s] == 1:
                needCount += 1

        for t in magazine:
            needMap[t] -= 1
            if needMap[t] == 0:
                needCount -= 1
        
        return bool(needCount == 0)

ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))

