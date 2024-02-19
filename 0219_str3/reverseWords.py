class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = []
        i = j = len(s) - 1
        while i >= 0:
            while i >=0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1: j + 1])
            while i>=0 and s[i] == " ":
                i -= 1
            j = i
        return " ".join(res)
s = "the sky is blue"
print(Solution().reverseWords(s))