class Solution:
    def sumoftwonumber(self,nums:list[int],target:int):
        sum_nums = 0
        i = 0
        j = len(nums)-1

        while i < j:
            sum_nums = nums[i] + nums[j]
            if sum_nums > target:
                j -= 1
            elif sum_nums < target:
                i += 1
            else:
                return [i+1,j+1]
        

numbers = [2,7,11,15]
target = 9

print(Solution().sumoftwonumber(numbers,target))