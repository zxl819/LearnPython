class Solution:
    def judgeCircle(self, moves: str):
        from collections import defaultdict
        check = defaultdict(int)
        check['U'] = 0
        check['D'] = 0
        check['L'] = 0
        check['R'] = 0
        for move in moves:
            check[move] += 1
        
        if check['U'] == check['D'] and check['L'] == check['R']:
            return True
        else:
            return False

moves = "UD"
print(Solution().judgeCircle(moves))

            
