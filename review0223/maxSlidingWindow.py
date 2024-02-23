class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int):
        from collections import deque
        n = len(nums)
        res = []
        q = deque()
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            #print(i, j)
            if i > 0 and nums[i - 1] == q[0]:
                q.popleft()
            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])
            if i >= 0:
                res.append(q[0])
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))