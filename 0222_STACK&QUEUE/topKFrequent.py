class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        from collections import Counter, deque
        cnt = Counter(nums)
        res = []
        tmp = deque()
        ans = []
        nums.sort()
        for i in nums:
            while res and cnt[i] > cnt[res[-1]]:
                tmp.append(res.pop())
            res.append(i)
            while tmp:
                res.append(tmp.pop())
        slow = 0
        ans.append(res[0])
        for i in range(len(res)):
            if res[slow] != res[i]:
                ans.append(res[i])
                slow = i
            else:
                i += 1

        return ans
    
nums = [5,3,1,1,1,3,5,73,1]
k = 3
print(Solution().topKFrequent(nums, k))