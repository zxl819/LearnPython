class Solution:
    def createMatrix(self, n:int):
        matrix = [[0]* n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1

        for offset in range(1, loop + 1):
            # 从左到右
            for i in range(startx, n - offset):
                matrix[startx][i] = count
                count += 1
            # 从上到下
            for i in range(starty, n - offset):
                matrix[i][n - offset] = count
                count += 1
            # 从右到左
            for i in range(n - offset, starty, -1):
                matrix[n - offset][i] = count
                count += 1
            # 从下到上
            for i in range(n - offset, startx, -1):
                matrix[i][starty] = count
                count += 1
            
            starty += 1
            startx += 1
        if n % 2 != 0:
            matrix[mid][mid] = count
        return matrix
    
n = 4

print(Solution().createMatrix(n))

