class Solution:
    def sortedArraySquare(self, nums: list[int]):
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        new = [0] * len(nums)

        while (i <= j):
            if nums[i] ** 2 > nums[j] **2:
                new[k] = nums[i] ** 2
                k -= 1
                i += 1
            else:
                new[k] = nums[j] ** 2
                k -= 1
                j -= 1
        return new
nums = [-4,-1,0,3,10]
print(Solution().sortedArraySquare(nums))