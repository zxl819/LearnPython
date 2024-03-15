class Solution:
    def SpiralArray(self, array: list[list[int]]):
        if not array:
            return []
        
        l, r, t, b = 0, len(array[0]), 0, len(array)
        res = []
        while True:
            for i in range(l, r):
                res.append(array[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b):
                res.append(array[i][r - 1])
            r -= 1
            if l > r:
                break
            for i in range(r - 1, l - 1, -1):
                res.append(array[b - 1][i])
            b -= 1
            if t > b:
                break
            for i in range(b - 1, t - 1, -1):
                res.append(array[i][l])
            l += 1
            if l >= r:
                break
        return res
array = [[1,2,3],[8,9,4],[7,6,5]]
print(Solution().SpiralArray(array))