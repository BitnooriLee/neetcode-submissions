class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        row_0 = any(matrix[0][i] == 0 for i in range(n))
        col_0 = any(matrix[i][0] == 0 for i in range(m))

        

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 
                    matrix[i][0] = 0 


        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0 
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0 
        if row_0:
            for j in range(n):
                    matrix[0][j] = 0 
        if col_0:
            for i in range(m): #그 col을 0으로 
                    matrix[i][0] = 0 
