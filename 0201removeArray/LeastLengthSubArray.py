class Solution:
    def LeastLengthArray(self, nums: list[int],s: int):
        if sum(nums) < s:
            return 0
        l = 0
        sum = 0
        min_length = float("inf")
        for r in range(len(nums)):
            sum += nums[r]
            while(sum >= s):
                sum -= nums[l]
                min_length = min(min_length, r - l + 1)
                l += 1
        return min_length    
    

s = 7
nums = [2,3,1,2,4,3]   
print(Solution().LeastLengthArray(nums, s))                