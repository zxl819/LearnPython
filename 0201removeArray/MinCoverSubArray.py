class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        subArray = []

        for r in range(len(s)):
            subArray.append(s[r])
            for x in t:
                while x in subArray:
                    while (l < len(subArray) ):
                        subArray.pop()
                        l += 1

