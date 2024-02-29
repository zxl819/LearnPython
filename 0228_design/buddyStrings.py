class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter
        if len(s) != len(goal):
            return False
        
        changeS = []
        changeG = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                changeS.append(s[i])
                changeG.append(goal[i])
            
        if not changeS:
            return False 
        elif changeS[1] == changeG[0] and changeS[0] == changeG[1]:
            return True
        else:
            return False
from collections import Counter
s = "ab"
goal = "ab"
print(Counter(s))

print(Solution().buddyStrings(s, goal))            
            