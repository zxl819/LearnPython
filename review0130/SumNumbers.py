class Solution:
    def SumNumbers(self,numbers:list[int],target:int):
        i = 0
        j = len(numbers)-1
        sum_nums = 0

        while i < j:
            sum_nums = numbers[i] + numbers[j]
            if sum_nums > target:
                j -= 1
            elif sum_nums < target:
                i += 1
            else:
                return [i+1,j+1]

numbers = [2,7,11,15]
target = 9
print(Solution().SumNumbers(numbers,target))