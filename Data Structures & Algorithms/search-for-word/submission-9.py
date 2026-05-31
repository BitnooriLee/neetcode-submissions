class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        visit = set()
        def bt(i,j,k):
            if k == len(word):
                return True
            for di,dj in move:
                ni, nj = i+di, j+dj 
                
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visit and board[ni][nj] == word[k]:
                    visit.add((ni,nj))
                    if bt(ni,nj,k+1):
                        return True
                    visit.remove((ni,nj))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit.add((i,j))
                    if bt(i,j,1):
                        return True
                    visit.remove((i,j))
        return False
        