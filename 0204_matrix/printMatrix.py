class Solution:
    def printMatrix(self, matrix: list[int]):
        startx, starty = 0, 0
        m = len(matrix) #3
        n = len(matrix[0]) #4 
        loop = max(len(matrix) // 2 ,  len(matrix[0]) // 2)
        ans = []

        if n == 1 or m == 1:
            return matrix

        for offset in range(1, loop + 1):
            # 从左到右
            for i in range(starty, n - offset):
                ans.append(matrix[startx][i])
            # 从上到下
            for i in range(startx, n - offset):
                ans.append(matrix[i][n - offset])
            # 从右到左
            for i in range(m - offset, starty, -1):
                ans.append(matrix[m - offset][i])
            # 从下到上
            for i in range(m - offset, startx, -1):
                ans.append(matrix[i][starty])

            
            if startx < loop:
                startx += 1
                starty += 1
            else:
                break
        if m == n and m % 2 != 0:
            ans.append(matrix[loop][loop])
        return ans
        
matrix = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(Solution().printMatrix(matrix))