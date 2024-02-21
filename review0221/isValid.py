class Solution:
    def isValid(self, s: str):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if not stack or c != stack[-1]:
                    return False
                stack.pop()
        return True

s = "()[]{}"
print(Solution().isValid(s))
    
