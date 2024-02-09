class Solution:
    def plusOne(self, digits: list[int]):
        res = 0
        ans = list()
        for i in range(len(digits)):
            res += digits[i] * (10 ** (len(digits) - i - 1))
        res += 1
        ans.append(res // 10 ** (len(digits) - 1))
        if digits[0] == 9:
            for i in range(1, len(digits)):
                ans.append(res // 10 ** (len(digits) - i) - ans[i] * 10 ** (len(digits) - i))
        else:
            for i in range(1, len(digits)):
                ans.append(res // (10 ** (len(digits) - i - 1)) - ans[i - 1] * 10 ** (len(digits)- i - 1))
        return ans



    

digits = [1,2,3]
print(Solution().plusOne(digits))