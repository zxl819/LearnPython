class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        from collections import defaultdict
        n1 = defaultdict(int)
        n2 = defaultdict(int)
        for i in nums1:
            n1[i] += 1
        res = []
        for i in n1:
            if i in nums2:
                res.append(i)
        return res
    
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))