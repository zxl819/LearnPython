class Solution:
    def maxArea(self, height: list[int]):
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
              area =max(area, (j - i) * min(height[i], height[j]))
              if height[i] > height[j]:
                   j -= 1
              else:
                   i += 1
        return area
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
            

              