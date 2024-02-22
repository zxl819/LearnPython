from operator import add, mul, sub 
class Solution:
    op_mat = {'+': add, '-': sub, '*': mul, '/': lambda x,y: int(x/y)}
    def evalRPN(self, tokens: list[str]):
        res = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                res.append(int(token))
            else:
                op1 = res.pop()
                op2 = res.pop()
                res.append(self.op_mat[token](op2, op1))
        return res

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens)) 

