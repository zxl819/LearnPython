class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]):
        from collections import defaultdict
        res = defaultdict(int)
        for n1 in nums1:
            res[n1] += 1
        cnt = []
        
        for i in nums1:
            if i in nums2:
                cnt.append(i)
                res[i] -= 1
                if res[i] == 0:
                    del res[i]
        return cnt

