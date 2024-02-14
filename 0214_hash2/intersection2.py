class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]):
        from collections import defaultdict
        l1_Cnt = defaultdict(int)
        l2_Cnt = defaultdict(int)
        res = []
        for num1 in nums1:
            l1_Cnt[num1] += 1
        
        for num2 in nums2:
            l2_Cnt[num2] += 1
        
        for x in l1_Cnt:
            i = 0
            if x in l2_Cnt:
                while i < min(l1_Cnt[x], l2_Cnt[x]):
                    res.append(x)
                    i += 1
        return res
    
nums1 = [1, 2, 2, 1]
nums2 = [9,0,9,8,4]
print(Solution().intersect(nums1, nums2))
