class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """
        from collections import defaultdict
        check = defaultdict(int)
        row = []
        col = []
        row_zero = []
        col_zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_zero.append(i)
                    col_zero.append(j)        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        return matrix
        
    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(Solution().setZeroes(matrix))
        