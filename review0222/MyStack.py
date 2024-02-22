from collections import deque
class MyStack:
    def __init__(self):
        self.stack = deque()

    def empty(self):
        return not self.stack
    
    def push(self, x: int):
        self.stack.append(x)
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        ans = self.pop()
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft)
        self.stack.append(ans)
        return ans
