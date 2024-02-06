class Solution:
    def spiralOrder(self, matrix: list[list[int]]):
        if not matrix:
            return []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []

        while True:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            if t >= b:
                break
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            if l >= r:
                break
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            if t >= b:
                break
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l >= r:
                break
        return res
matrix =[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
print(Solution().spiralOrder(matrix))
