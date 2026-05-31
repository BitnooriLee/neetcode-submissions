class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        v = set()
        h = set()
        dia = set()
        dia2 = set()

        path = [["."]*n for _ in range(n)]
        output = []
        def bt(i):
            if i == n:
                output.append(["".join(row) for row in path])
                return
            for j in range(n):
                if i not in v and j not in h and i+j not in dia and (i-j) not in dia2:
                    v.add(i)
                    h.add(j)
                    dia.add(i+j)
                    dia2.add(i-j)
                    path[i][j] = "Q"
                    bt(i+1)
                    path[i][j] = "."
                    v.remove(i)
                    h.remove(j)
                    dia.remove(i+j)
                    dia2.remove(i-j)
        
        bt(0)
        return output





        