from collections import deque
class MyStack:
    def __init__(self):
        self.que = deque()
    
    def empty(self):
        return not self.que
    
    def push(self, x: int):
        self.que.append(x)


    def pop(self):
        if self.empty():
            return None
        # for i in range(len(self.que) - 1):
        #     self.que.append(self.que.popleft())
        # return self.que.popleft()
        return self.que.pop()
    
    def top(self):
        ans = self.pop()
        self.que.append(ans)
        return ans
    

a = MyStack()
a.push(1)
a.push(2)
a.push(3)
print(a)

print(a.pop())
print(a.top())

    
    


        