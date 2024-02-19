class Solution:
    def tictactoe(self, moves: list[list[int]]):
        from collections import Counter
        n = len(moves)
        rowA = []
        rowB = []
        colA = []
        colB = []

        if n == 9:
            print("Draw")
            return 0
        for i in range(n):
            if i % 2 == 0:
                rowA.append(moves[i][0])
                colA.append(moves[i][1])
            else:
                rowB.append(moves[i][0])
                colB.append(moves[i][1])
        
        if len(rowA)== 3 and len(colA)== 3 and (rowA == colA or len(Counter(rowA)) == 1 or len(Counter(colA)) == 1):
            print("A")
        elif len(rowB)== 3 and len(colB)== 3 and (Counter(rowB) == Counter(colB) or len(Counter(rowB)) == 1 or len(Counter(colB)) == 1):
            print("B")
        else:
            print("Pending")
        
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Solution().tictactoe(moves)

