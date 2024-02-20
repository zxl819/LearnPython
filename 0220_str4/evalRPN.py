class Solution:
    from operator import add, sub, mul
    op_mat = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}
    def evalRPN(self, tokens: list[str]):
        stack = []
        res = 0
        for i in tokens:
            if i == "+":
                res = (int(stack.pop()) + int(stack.pop()))
                stack.append(res)
            elif i == "-":
                res = (-stack.pop() + stack.pop())
                stack.append(res)
            elif i == "*":
                res = (stack.pop() * stack.pop())
                stack.append(res)
            elif i  == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(i))
        return res
    def evalRPN2(self, tokens: list[str]):
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_mat[token](op1, op2))
        return stack.pop()

    
tokens = ["0","3","/"]
print(Solution().evalRPN(tokens))
