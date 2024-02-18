class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]):
        from collections import defaultdict
        check = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                check[n1 + n2] += 1
        
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                res += check[key]
        
        return res