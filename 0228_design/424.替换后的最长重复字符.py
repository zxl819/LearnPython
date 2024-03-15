#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        # l = 0
        # maxLen = 1
        # needCnt = 0
        # needmap = defaultdict(int)
        
        # res = deque()
        # for r in range(len(s)):
        #     needmap[s[r]] += 1
        #     if needmap[s[r]] == 1:
        #         # needCnt += 1
        #         res.append(s[r])
            
        #     if len(res) > 2:
        #         break


        #     # print(needmap[res[0]])
        #     if len(res) > 1 and min(needmap[res[0]], needmap[res[1]]) > k:
        #         maxLen = max(maxLen, needmap[res[0]]+ needmap[res[1]] - 1)
        #         needmap[s[l]] -= 1
        #         if needmap[s[l]] == 0:
        #             res.popleft()
        #         l += 1
        #     else:
        #         maxLen = sum(needmap.values())
        # return maxLen

        N = len(s)
        l, r = 0, 0
        cnter = Counter()
        res = 0
        while r < N:
            cnter[s[r]] += 1
            while r - l + 1 - cnter.most_common(1)[0][1] > k:
                cnter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
        

s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))
            


# @lc code=end

