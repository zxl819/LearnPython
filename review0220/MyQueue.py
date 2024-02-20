class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
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
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    
    def empty(self) -> bool:
        return not(self.stack_out or self.stack_in)