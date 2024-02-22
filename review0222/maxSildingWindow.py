from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int):
        n = len(nums)
        q = deque()
        res = []
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            if i > 0 and nums[i - 1] == q[0]: # 去除窗口外的数值
                q.popleft()
            while q and q[-1] < nums[j]:  # 生成一个有序的对列，比接下来加入的小的话，就去掉
                q.pop()
            q.append(nums[j])
            if i >= 0:
                res.append(q[0]) # i>0之后，窗口开始
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

