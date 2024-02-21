class Solution:
    from operator import add, sub, mul 
    op_mat = {'+': add, '-': sub, '*': mul, '/': lambda x,y : int(x/y)}
    def evalRPN(self, tokens: list[str]):
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.op_mat[token](op2, op1))
        return stack.pop()
            
            
