class Solution:
    def addBinary(self, a: str, b: str):
        i, j =len(a) - 1, len(b) - 1
        res = []
        k = 0
        while i >= 0 or j >= 0:
            a_i = int(a[i]) if i >= 0 else 0
            b_i = int(b[j]) if j >=0 else 0
            tmp, k = self.add(a_i, b_i,  k)
            res.append(tmp)
            j -= 1
            i -= 1
        if k != 0:
            res.append(k)

        return ''.join(map(str, reversed(res)))
    def add(self, a_i: int, b_i: int, k: int):
        tmp =  a_i + b_i + k
        return (tmp % 2, tmp // 2)

        


a = "1"
b = "11"
print(Solution().addBinary(a, b))

