class Solution:
    def lemonadeChange(self, bills: list[int]):
        from collections import defaultdict
        changes = defaultdict(int)
        for i in range(len(bills)):
            changes[bills[i]] += 1
            if bills[i] > 5:
                need = bills[i] - 5
                if need < sum(changes):
                    changes[need] -= 1
                    if changes[need] == 0:
                        del changes[need]
                else: return False
        return True
    
bills = [5,5,5,10,20]
print(Solution().lemonadeChange(bills))