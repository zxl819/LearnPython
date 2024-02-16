class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        from collections import Counter
        n1 = Counter(nums1)
        res = []
        for x in n1:
            if x in nums2:
                res.append(x)
        return res
    def intersection2(self, nums1: list[int], nums2: list[int]):
        from collections import defaultdict
        n1 = defaultdict(int)
        n2 = defaultdict(int)
        for n in nums1:
            n1[n] += 1
        for n in nums2:
            n2[n] += 1
        res = []
        for x in n1:
            while n2[x] != 0 and n1[x] != 0:
                res.append(x)
                n2[x] -= 1
                n1[x] -= 1
                if n2[x] == 0:
                    del n2[x]
        return res


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection2(nums1, nums2))