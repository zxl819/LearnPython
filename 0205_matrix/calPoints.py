class Solution:
    def calPoints(self, operations: list[str]):
        tmp = []
        k = 0
        for i in range(len(operations)):
            if operations[i] == 'C':
                tmp.pop()
                k -= 1
            elif operations[i] == 'D':
                tmp.append(int(tmp[k-1])*2)
                k += 1
            elif operations[i] == "+":
                tmp.append(int(tmp[k-1]) + int(tmp[k-2]))
                k += 1
            else:
                tmp.append(int(operations[i]))
                k += 1
        return sum(tmp)
    
ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints(ops))