class Solution:
    def removeDuplicates(self, s: str):
        stack = []
        for i in range(len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i]) # 条件
        return "".join(stack)
    
s = "abbaca"
print(Solution().removeDuplicates(s))

            
