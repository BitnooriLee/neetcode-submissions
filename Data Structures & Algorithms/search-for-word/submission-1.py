class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        move = [[0,1],[0,-1],[1,0],[-1,0]]
        
        # true -> keep dfs
        # false -> return false 
        def dfs(i,j,cur):
            if cur == len(word):
                return True

            #out of bound or ch is different 
            if 0>i or i>=len(board) or 0>j or j>=len(board[0]) or board[i][j]!= word[cur]:
                   return False

            # if it's visited -> return False 
            # before/after for loop, need to mark board[i][j] (previous val)
            tmp = board[i][j]
            board[i][j] = ''
            for dx,dy in move:
                x,y = i+dx,j+dy
                #if board[x][y]:
                if dfs(x,y,cur+1):
                    return True
            board[i][j] = tmp 
            return False 



        for i in range(len(board)):
            for j in range(len(board[0])):
                # dfs False -> nothing happen
                if dfs(i,j,0):
                    return True

        return False
        