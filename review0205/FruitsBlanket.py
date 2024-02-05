from collections import defaultdict
class Solution:
    def fruitsBlanket(self, fruits: list[int]):
        classMap = defaultdict(int)
        classCount = 0
        i, j = 0, 0
        res = 0

        for j in range(len(fruits)):
            classMap[fruits[j]]+= 1
            if classMap[fruits[j]] == 1:
                classCount += 1
            
            while classCount > 2:
                classMap[fruits[i]] -= 1
                if classMap[fruits[i]] == 0:
                    classCount -= 1
                i += 1
            
            res = max(res, j - i + 1 )
        return res
            

fruits = [1,2,1]
print(Solution().fruitsBlanket(fruits))


