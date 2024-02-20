class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int):
        win = []
        slow = 0
        res =[]
        for fast in range(len(nums)):
            if fast - slow + 1 == k:
                win = nums[slow: fast + 1]
                res.append(max(win))
                slow += 1
        return res
    
    def maxSlidingWindowQue(self, nums: list[int], k: int):
        from collections import deque
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)

            if i - q[0] >= k:
                q.popleft()
            
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


    
nums = [1]
k = 1
print(Solution().maxSlidingWindow(nums, k))
                
