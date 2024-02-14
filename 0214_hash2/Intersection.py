class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        from collections import defaultdict
        l1_Cnt = defaultdict(int)
        l2_Cnt = defaultdict(int)
        res = []
        for num1 in nums1:
            l1_Cnt[num1] += 1
        
        for num2 in nums2:
            l2_Cnt[num2] += 1
        
        for x in l1_Cnt:
            if x in l2_Cnt:
                res.append(x)
        return res
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))