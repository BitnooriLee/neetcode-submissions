class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board) # 9 

        for i in range(n):
            setR = set()
            for j in range(n):
                if board[i][j] ==".":
                    continue
                if board[i][j] in setR:
                    return False
                setR.add(board[i][j])

        for j in range(n):
            setC = set()
            for i in range(n):
                if board[i][j] ==".":
                    continue
                if board[i][j] in setC:
                    return False
                setC.add(board[i][j])

        

      
        for m in range(0,3):
            for n in range(0,3):
                setRC = set()
                for i in range(0,3): 
                    for j in range(0,3): 
                        if board[3*m+i][3*n+j] ==".":
                            continue
                        if board[3*m+i][3*n+j] in setRC:
                            return False
                        setRC.add(board[3*m+i][3*n+j])
            
        return True

                
        