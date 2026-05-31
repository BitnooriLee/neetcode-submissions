class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        move = [(0,1), (0,-1), (1,0), (-1,0)]
        visit = set()

        def bt(x,y,l):
            if (x,y) in visit:
                return False
            if board[x][y] != word[l]:
                return False
            if l == len(word)-1:
                return True
            visit.add((x,y))
            for dx,dy in move:
                nx,ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n:
                    if board[nx][ny] == word[l+1]:
                        if bt(nx,ny,l+1):
                            return True
            visit.remove((x,y))
            return False

            


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bt(i,j,0):
                        return True
    
        return False 
        