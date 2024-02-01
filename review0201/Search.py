class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid  = l + (r - l) // 2
            mid2 = (l + r) // 2 #二者似乎相同
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1

Solution().search([1, 3, 5, 6, 8, 10, 11],9)