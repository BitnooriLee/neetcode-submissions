class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        seen = [[False]*n for _ in range(m)]
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        def bt(i,j,k):
            if k == len(word):
                return True
            if i >=m or i <0 or j <0 or j >=n:
                return False
            if seen[i][j] or board[i][j] != word[k]:
                return False
            seen[i][j] = True
            for di,dj in move:
                if bt(i+di,j+dj,k+1):
                    return True
            seen[i][j] = False
            return False
            
        for i in range(m):
            for j in range(n):
                if bt(i,j,0):
                    return True
        return False
        