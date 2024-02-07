class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while j >= i:
            if height[i] < height[j]:
                res = max(res, (j - i) * min(height[i],height[j]))
                i += 1
            else:
                res = max(res, (j - i) * min(height[i],height[j]))
                j -= 1
        return res


height = [1,8,6,2,5,4,8,3,7]
print(min(height[1],height[2]))
print(Solution().maxArea(height))