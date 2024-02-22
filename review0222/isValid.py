class Solution:
    def isValid(self, s:str):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:
                if stack[-1] != c:
                    return False
                stack.pop()
        return True if not stack else False
                