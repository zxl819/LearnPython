class Solution:
    def plusOne(self, digits: list[int]):
        res = 0
        ans = []
        for i in range(len(digits)):
            res += digits[i] * (10 ** (len(digits)- i - 1))
        
        res += 1
        new = str(res)
        for i in new:
            ans.append(int(i))
        return ans
    
digits = [1,2,3]
print(Solution().plusOne(digits))
            