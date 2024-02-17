class Solution:
    def reverseStr(self, s: str, k: int):
        n = len(s)
        l = 0
        while n > 0:
            if n < k:
                s = reversed(s)
                return res
            elif n < 2 * k:
                for i in range(k):
                    s[i], s[k - 1 - i] = s[k - 1 - i], s[i]
                return res
            else:
                for i in range(l, k):
                    s[i], s[k - 1 - i] = s[k - 1- i], s[i]
                n -= 2*k
                l += 2*k
        
        return s



            
