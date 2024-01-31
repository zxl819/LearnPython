class Solution: #错误解法，部分返回的会小，分析一下,还是得调试
    def mysqrt(self, x: int):
        l , r = 0, x
        while (l <= r):
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return mid - 1 if mid * mid > x else mid 
            
print(Solution().mysqrt(6))