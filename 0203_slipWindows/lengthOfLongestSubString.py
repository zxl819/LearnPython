class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, res= 0, 0, 0
        ans = []

        while j < len(s) :
            if s[j] not in ans:
                ans.append(s[j])
                res = max(res, len(ans))
                j += 1
            else: 
                ans = list(s[i : j])
                res = max(res, len(ans))
                if ans != []:
                    del ans[0]
                i += 1
        return res

s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
