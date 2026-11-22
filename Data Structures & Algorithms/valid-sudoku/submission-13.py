class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        m,n = len(board), len(board[0])
       
        for i in range(m): 
            seen_n = set()      
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_n:
                    return False
                seen_n.add(board[i][j])
                
        for j in range(n):
            seen_m = set()       
            for i in range(m):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_m:
                    return False
                seen_m.add(board[i][j])

        for br in range(m//3):
            for bc in range(n//3):
                seen_m = set()
                for j in range(m//3):
                    for k in range(n//3):
                        if board[br*3+j][bc*3+k] == ".":
                            continue
                        if board[br*3+j][bc*3+k] in seen_m:
                            return False
                        seen_m.add(board[br*3+j][bc*3+k])
        return True 
