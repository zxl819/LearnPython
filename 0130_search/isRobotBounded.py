class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        k = 0
        dist = [0] * 4  # 先抽象出来找规律
        for i in instructions:
            if i == 'L':
                k = (k + 1) % 4
            elif i == 'R':
                k = (k + 3) % 4
            else:
                dist[k] += 1
        return (dist[0] == dist[2] and dist[1] == dist[3]) or k != 0
                



                     

