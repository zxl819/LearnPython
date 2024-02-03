
class Solution:
    def numsSquare(self, nums: list[int]):
        i, j, k = 0, len(nums) - 1, len(nums) -1
        new = [float("inf")] * len(nums)
        while (i <= j):
            if nums[i] ** 2 <= nums[j] ** 2:
                new[k] = nums[j] ** 2
                j -= 1
                k -= 1
            else:
                new[k] = nums[i] ** 2
                i += 1
                k -= 1
        return new
nums = [-4,-1,0,3,10]
print(Solution().numsSquare(nums))
            


        