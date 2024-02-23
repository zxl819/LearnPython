class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        grad = []
        # n = len(coordinates)
        for i in range(1, len(coordinates)):
            if coordinates[i][0] == coordinates[i - 1][0]:
                grad.append(0)
        if len(grad) == len(coordinates) - 1:
            return True
        elif grad:
            return False

                
        for i in range(2, len(coordinates)):
            gradient = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            if gradient != (coordinates[i][1] - coordinates[i - 1][1])/(coordinates[i][0] - coordinates[i - 1][0]):
                return False
            
        return True

coordinates = [[0,0],[0,1],[0,-1]]
print(Solution().checkStraightLine(coordinates))

        