class Solution:
    def minLengthSubarray(self,target:int,nums:list[int]):
        if sum(nums) < target:
            return 0
        i = 0 
        sum_nums = 0
        min_length = float('inf')
        for j in range(len(nums)):
            sum_nums +=  nums[j] # 逻辑
            while sum_nums >= target:
                min_length = min(min_length, j - i + 1)  #先要存储结果
                sum_nums -= nums[i]
                i += 1 #这个之后条件可能不能满足
                
            
        
        return min_length


target = 7
nums = [2,3,1,2,4,3]

print(Solution().minLengthSubarray(target,nums))
