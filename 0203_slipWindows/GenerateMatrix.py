class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        nums = [[0] * n for _ in range(n)] # 这是一个列表推导式，用于生成列表。
        startx, starty = 0, 0
        loop, mid = n // 2, n // 2
        count = 1

        for offset in range(1, loop + 1):
            # 从左到右
            for i in range(startx, n - offset):
                nums[startx][i] = count
                count += 1
            # 从上到下
            for i in range(starty, n - offset):
                nums[i][n - offset] = count
                count += 1
            # 从右到左
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1
            
            startx += 1
            starty += 1

        if n % 2 != 0:
            nums[mid][mid] = count
        return nums



print(Solution().generateMatrix(3))