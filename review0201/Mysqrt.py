import math
class Solution:
    def mysqrt (self, x: int):
        ans = int(math.exp(0.5 * math.log(x)))

        return ans if ans * ans <= x else ans - 1