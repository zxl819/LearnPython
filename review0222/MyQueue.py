class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def empty(self):
        return not(self.stack_in or self.stack_out)
    
    def push(self, x: int):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
    def peek(self):
        if self.empty():
            return None
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    
    



a = MyQueue()
a.push(1)
a.push(2)
a.push(3)
print(a.empty())
print(a.pop())
print(a.peek())
print(a.pop())

