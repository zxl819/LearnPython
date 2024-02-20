class Solution:
    def isValid(self, s: str):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            
            elif not stack or s[i] != stack[-1]:
                return False
            else:
                stack.pop()
        return True if not stack else False #最后查看stack是否为空
    
s = "[()]"
print(Solution().isValid(s))