class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        N = str(n)
        rev_s = ""
        for i in N:
            if i not in dic:
                return False
            rev_s = dic[i] + rev_s
        return rev_s != N


        




n = 379
print(Solution().confusingNumber(n))