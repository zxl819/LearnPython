# 左开右闭
class Solution:
    def spiralOrder(self, matrix: list[list[int]]):
        if not matrix:
            return []
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        res = []

        while True:
            # 从左到右
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # 从上到下
            if t >= b:
                break
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            if l >= r:
                break
            # 右到左
            # if l > r:
            #     break
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            if t >= b:
                break

            # 从下到上
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l >= r:
                break

        
        return res

matrix = [[2,3]]
print(Solution().spiralOrder(matrix))
            
            

    