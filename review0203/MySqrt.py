class Solution:
    def mysqrt(self, x: int):
        l, r = 0, x
        while (l <= r):
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return l - 1

            