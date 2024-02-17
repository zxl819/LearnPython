class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat[0])
        res = 0
        if n % 2 != 0:
            mid = n // 2
            for i in range(n):
                res += mat[i][i] + mat[i][n-i-1] 
            res -= mat[mid][mid]
        else:
            for i in range(n):
                res += mat[i][i] + mat[i][n-i-1] 
        return res

