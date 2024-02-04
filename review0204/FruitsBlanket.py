from collections import defaultdict
class Solution:
    def fruitsBlanket (self, fruits: list[int]):
        classMap =  defaultdict(int)
        classCount = 0
        i, j = 0, 0
        res = 0

        for j in range(len(fruits)):
            classMap[fruits[j]] += 1  #条件弄错
            if classMap[fruits[j]] == 1:
                classCount += 1
                
            while classCount > 2: # 当条件不满足的时候，找到合适的窗口
                classMap[fruits[i]] -= 1
                if classMap[fruits[i]] == 0:
                    classCount -= 1
                i += 1
            res = max(res, j - i + 1) # 放错位置
        return res
    
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().fruitsBlanket(fruits))

