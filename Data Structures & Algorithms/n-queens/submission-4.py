class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        path = [["."]*n for _ in range(n)] #한개의 판 
        col = set()
        dig1 = set()
        dig2 = set()
        row = set()
        def bt(i):
            if i == n:
                output.append(["".join(row) for row in path])
                return 
            for j in range(n):
                if (i not in col) and (j not in row) and (i+j) not in dig1 and (i-j) not in dig2:
                    col.add(i)
                    row.add(j)
                    dig1.add(i+j)
                    dig2.add(i-j)
                    path[i][j] = "Q"
                    bt(i+1)
                    path[i][j] = "."
                    col.remove(i)
                    row.remove(j)
                    dig1.remove(i+j)
                    dig2.remove(i-j)

        bt(0)
        return output