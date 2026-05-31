class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        set_c = set()
        set_r = set()
        for i in range(m):
            for j in range(n):
                if (i not in set_c or j not in set_r) and matrix[i][j] == 0:
                    set_c.add(i)
                    set_r.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in set_c or j in set_r:
                    matrix[i][j] = 0 




        
        