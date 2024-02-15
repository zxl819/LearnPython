class Solution:
    def fourSum(self, nums: list[int], target: int):
        nums.sort()
        res = []
        n = len(nums)
        r = n - 1
        if not nums or n < 4:
            return res
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # 跳过重复值
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: # 跳过重复的值
                    continue
                l, r = j+1, n-1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r = r - 1
                    elif total < target:
                        l = l + 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while (l < r and nums[l] == nums[l + 1]):
                            l += 1
                        while (r > l and nums[r] == nums[r - 1]):
                            r -= 1
                        l += 1
                        r -= 1
        return res
nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums, target))

def four_sum(nums, target):
    nums.sort() # 对数组进行排序
    result = []
    n = len(nums)
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: # 跳过重复的值
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]: # 跳过重复的值
                continue
            l, r = j+1, n-1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # 跳过重复的值
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # 跳过重复的值
                        r -= 1
                    l += 1
                    r -= 1
    return result

# 测试示例
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
nums2 = [2, 2, 2, 2, 2]
target2 = 8

result1 = four_sum(nums1, target1)
result2 = four_sum(nums2, target2)

result1, result2
