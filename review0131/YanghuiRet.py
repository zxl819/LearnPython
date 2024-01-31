class Solution:
    def YanghuiRet(self, numRows: int):
        ret = []
        for i in range(numRows):
            row = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j-1])
                    
            ret.append(row)
        return ret
    

numRows = 5
print(Solution().YanghuiRet(5))