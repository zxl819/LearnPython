class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        from collections import Counter
        c = Counter(nums)
        a = c.most_common(k)
        return (a1[0] for a1 in a)