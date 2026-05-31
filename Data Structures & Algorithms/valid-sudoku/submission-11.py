class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        dic_c = defaultdict(set)
        dic_r = defaultdict(set)
        dic_rc = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dic_c[i]:
                    return False
                dic_c[i].add(board[i][j])
                if board[i][j] in dic_r[j]:
                    return False
                dic_r[j].add(board[i][j])
                if board[i][j] in dic_rc[(i//3, j//3)]:
                    return False
                dic_rc[((i//3, j//3))].add(board[i][j])
        return True
                

        