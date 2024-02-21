from collections import deque
class MyStack:
    def __init__(self):
        self.que = deque()
    
    def empty(self):
        return not self.que
    
    def push(self, x: int):
        self.que.append(x)
    
    def pop(self):
        return self.que.pop()
    
    def top(self):
        ans = self.pop()
        self.que.append(ans)
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return ans
    
a = MyStack()
a.push(1)
a.push(2)
print(a.top())
print(a.pop())
print(a.top())
print(a.empty())

