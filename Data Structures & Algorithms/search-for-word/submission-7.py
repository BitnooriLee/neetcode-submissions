class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        path = ""
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        def bt(i,j):
            nonlocal path
            if board[i][j] != word[len(path)]:
                return False
            tmp = board[i][j]
            path+=tmp
            if len(path) == len(word):
                return True
            board[i][j] = "#"
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj] != "#":
                        if bt(ni,nj):
                            return True #여기가 핵심
                    
            
            path = path[:-1]
            board[i][j] = tmp


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bt(i,j):
                        return True

        return False
