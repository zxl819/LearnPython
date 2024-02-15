class Solution:
    def threeSum(self, nums: list[int]):
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1 
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
            return res

def three_sum(nums):
    nums.sort() # 先对数组进行排序
    result = []
    n = len(nums)
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: # 跳过重复值
            continue
        l, r = i+1, n-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: # 跳过重复值
                    l += 1
                while l < r and nums[r] == nums[r-1]: # 跳过重复值
                    r -= 1
                l += 1
                r -= 1
    return result

# 测试示例
nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]

result1 = three_sum(nums1)
result2 = three_sum(nums2)
result3 = three_sum(nums3)

result1, result2, result3



        
        