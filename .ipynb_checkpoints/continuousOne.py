class Solution:
    def continuousOne(self,nums:list[int]):
        i = 0
        max_length = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                i += 1
                max_length = max(max_length, i) # 不能放另一个分支，否则会少输一个
            else:
                i = 0
        return max_length


nums = [1,1,0,1,1,1]
print(Solution().continuousOne(nums))
