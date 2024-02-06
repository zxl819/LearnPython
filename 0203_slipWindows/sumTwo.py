class Solution:
    def twoSum(self, nums: list[int], target: int):
        # 已通过，但时间复杂度为O（n^2）
        for i in range(len(nums)):
            sum_nums = 0
            j = len(nums) - 1
            while j > i:
                sum_nums = nums[i] + nums[j]
                if sum_nums == target:
                    return [i, j]
                j -= 1
                sum_nums = 0
 
    def twoSum_answer(self, nums: list[int], target: int):
        # 时间复杂度为O(n)
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i+1, :]:
                return [i, nums[i+1,:].index(res) + i + 1]


nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target))
            

