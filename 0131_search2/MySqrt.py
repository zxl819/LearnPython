import math
class Solution:
    def mysqrt(self, x: int):
        for i in range(x // 2 + 2):
            if i * i > x:
                return i - 1
            elif i * i == x:
                return i
        
    def mysqrtStandard1(self, x: int):
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))

        return ans + 1 if (ans + 1) ** 2 <= x else ans
    
    def mysqrtStandard2(self, x: int):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

        
print(Solution().mysqrt(8))
print(Solution().mysqrtStandard1(8))
print(Solution().mysqrtStandard2(8))




            

