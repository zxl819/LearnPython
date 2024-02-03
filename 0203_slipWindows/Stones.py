class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        i, j = 0, len(stones) - 1
        sum_left = 0
        sum_right = 0
        diff = float("inf")

        Alice_score = 0
        Bob_score = 0

        while(i <= j):
            if stones[i] < stones[j]:
                Alice_score = sum[stones] - stones[i]
                stones.pop(stones[i])
                i += 1
                Bob_score = 
            else:
                Alice_score = sum(stones) - stones[j]
                stones.pop(stones[j])
                j -= 1



