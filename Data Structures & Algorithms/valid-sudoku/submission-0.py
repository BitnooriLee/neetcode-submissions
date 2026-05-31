class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        m = len(board[0])
        res = []
        for i in range(l):
            for j in range(m):
                ele = board[i][j]
                if ele != ".":
                    res+= [(i,ele),(ele,j),(i//3,j//3,ele)]
        return len(res) == len(set(res))

                    

        