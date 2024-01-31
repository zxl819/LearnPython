class Solution:
    def isPerfectNumber (self, num: int):
        l, r = 0, num
        while (l <= r):
            mid = (l + r) // 2
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True
        return False
    
print(Solution().isPerfectNumber(1))
            
