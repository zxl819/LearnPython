from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j = 0
        subArray = defaultdict(int)
        cnt = 1
        for i in s:
            if i not in subArray:
                subArray[i] += 1
                cnt = max(cnt,len(subArray))
            else:
                cnt = max(cnt,len(subArray))
                while s[j] in subArray:
                    subArray[s[j]] -= 1
                    if subArray[s[j]] == 0:
                        del subArray[s[j]]
                    j += 1
                    if i not in subArray:
                        subArray[i] += 1
                        break
        return cnt
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))       
               
                
                
            

