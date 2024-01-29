class Solution:
    def zero_matrix(self,matrix:list[list[int]]):
        zero_row = []
        zero_column = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    zero_row.append(i)
                    zero_column.append(j)

        for i in range(len(matrix)):
            if i in zero_row:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if j in zero_column:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        return matrix

A = [
  [1,1,1],
  [1,0,1],
  [1,1,1]]    

sol = Solution()
B =  sol.zero_matrix(A)
print(B)