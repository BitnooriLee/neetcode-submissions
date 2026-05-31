class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [["."] * n for _ in range(n)] # n x n 
        r_set = set()
        c_set = set()
        r_c_set = set() # r-c
        r_c_set2 = set() # r+c 

        

        def bt(i):
            if i == n:
                res.append(["".join(row) for row in path])
                return 

            for j in range(n):
                if (i not in c_set) and (j not in r_set) and (i+j not in r_c_set2) and ((i-j) not in r_c_set):
                    c_set.add(i)
                    r_set.add(j)
                    r_c_set2.add(i+j)
                    r_c_set.add(i-j)
                    path[i][j] = "Q"
                    bt(i+1)
                    path[i][j] = "."

                    c_set.remove(i)
                    r_set.remove(j)
                    r_c_set2.remove(i+j)
                    r_c_set.remove(i-j)
            


        bt(0)
            

        return res 




        