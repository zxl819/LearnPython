class Solution:
    def generateMartrix(self, n: int):
        res = [[0]* n for _ in range(n)]
        l, r, t, b = 0, len(res[0]), 0, len(res)
        count = 1

        while True:
            for i in range(l, r):
                res[t][i] = count
                count += 1
            t += 1
            if t >= b:
                break
            for i in range(t, b):
                res[i][r - 1] = count
                count += 1
            r -= 1
            if l >= r:
                break
            for i in range(r - 1, l - 1, -1):
                res[b - 1][i] = count
                count += 1
            
            b -= 1
            if t >= b:
                break
            for i in range(b - 1, t - 1, -1):
                res[i][l] = count 
                count += 1
            l += 1
            if l >= r:
                break
        return res

print(Solution().generateMartrix(3))