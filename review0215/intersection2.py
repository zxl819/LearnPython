class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]):
        nums1.sort()
        nums2.sort()

        len1, len2 = len(nums1), len(nums2)
        inter = list()
        idx1, idx2 = 0, 0

        while idx1 < len1 and idx2 < len2:
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
            else:
                inter.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
        return inter
    
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersection(nums1, nums2))