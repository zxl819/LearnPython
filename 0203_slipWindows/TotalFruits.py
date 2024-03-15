from collections import defaultdict
class Solution:
    def totalFruits(self, fruits: list[int]):
        # 最大滑窗
        # 学习字典的用法
        i, j = 0, 0
        res = 0
        classMap = defaultdict(int)
        classCnt = 0
        
        # 移动滑窗右边界 
        while j < len(fruits):
            # 判断当前是否满足条件
            if classMap[fruits[j]] == 0:
                classCnt += 1
            classMap[fruits[j]] += 1

            # 若不满足条件，移动i
            while classCnt > 2:
                if classMap[fruits[i]] == 1:
                    classCnt -= 1
                classMap[fruits[i]] -= 1 # 按照fruits的顺序减去
                i += 1

            # 一旦满足条件，更新结果
            res = max(res, j - i + 1)
            j += 1
        return res
    


    def totalFruits2(self, fruits: list[int]):
        i, j = 0, 0
        res = 0
        classMap = defaultdict[int]
        classCount = 0

        while j < len(fruits):
            
            if classMap[fruits[j]] == 1:
                classCount += 1
            classMap[fruits[j]] += 1

            while classCount > 2:
                if classMap[fruits[i]] == 1:
                    classCount -= 1
                classMap[fruits[i]] -= 1
            i += 1
            
            res = max(res, j - i + 1)
            j += 1
        return res
            




fruits = [3,3,3,1,2,1,1,2,3,3,4]
Solution().totalFruits2(fruits)