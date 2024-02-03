class Solution:
    def minSubarray(self, target: int, nums: list[int]):
        if sum(nums) < target:
            return 0
        slow = 0
        ans = 0
        min_length = float("inf")

        for fast in range(len(nums)):
            ans += nums[fast]
            while ans >= target:
                ans -= nums[slow]
                min_length = min(min_length, fast - slow + 1)
                slow += 1
        return min_length

target = 4
nums = [1,4,4]
print(Solution().minSubarray(target, nums))
