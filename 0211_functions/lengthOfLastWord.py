class Solution:
    def lengthOfLastWord(self, s: str):
        word = s.split()
        return len(word[-1])
s = "Hello World"
print(Solution().lengthOfLastWord(s))