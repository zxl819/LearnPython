class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        from collections import Counter
        c = Counter(nums)
        tmp = c.most_common(k)
        return [t[0] for t in tmp]
    
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))