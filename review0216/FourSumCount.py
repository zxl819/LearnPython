class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        from collections import defaultdict
        checkList = defaultdict(int)
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                checkList[n1+n2] += 1
        
        for n3 in nums3:
            for n4 in nums4:
                key = -(n3 + n4)
                if key in checkList:
                    res += checkList[key] # 重复的数值组合
        
        return res
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
