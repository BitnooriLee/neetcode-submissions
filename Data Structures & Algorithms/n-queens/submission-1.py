class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        n # 0...n-1
        res = [] 
        path = [['.']*n for _ in range(n)] #주의! 
    
        cols = set()
        d1 = set() # i-j
        d2 = set() # i+j
   

        def backtracking(r):
            if r == n:
                res.append(["".join(row) for row in path])
                return
            for c in range(n):
                if c in cols or r-c in d1 or r+c in d2:
                    continue
            
                path[c][r] = "Q"
                cols.add(c)
                d1.add(r-c)
                d2.add(c+r)
                backtracking(r+1)

                path[c][r] = "."
                cols.remove(c)
                d1.remove(r-c)
                d2.remove(c+r)


        backtracking(0)

        return res 

        