class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        from collections import Counter
        n1 = Counter(nums1)
        res = []
        for i in nums2:
            if i in n1:
                res.append(i)
        return res
