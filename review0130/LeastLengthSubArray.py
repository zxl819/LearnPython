class Solution:
    def LeastLengthSubArray(self,nums:list[int],target:int):
        if sum(nums) < target:
            return 0
        
        slow = 0
        sum_nums = 0
        LeastLength = float("inf")

        for fast in range(len(nums)):
            sum_nums += nums[fast]

            while sum_nums >= target:
                sum_nums -= nums[slow]
                LeastLength = min(LeastLength, fast - slow + 1)
                slow += 1
        
        return LeastLength

target = 7
nums = [2,3,1,2,4,3]
print(Solution().LeastLengthSubArray(nums,target))

                

