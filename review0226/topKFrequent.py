class Solution:
    def topKFrqequent(self, nums: list[int], k: int):
        from collections import Counter
        c = Counter(nums)
        k = c.most_common(k)
        return [t[0] for t in k]