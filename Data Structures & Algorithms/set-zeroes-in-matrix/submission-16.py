class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m,n = len(matrix), len(matrix[0])

        z_row = any(matrix[0][i] == 0 for i in range(n))
        z_col = any(matrix[i][0] == 0 for i in range(m))
        
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0 
                    
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0 

        if z_col:
            for i in range(0,m):
                matrix[i][0]= 0 
        if z_row:
            for j in range(0,n):
                matrix[0][j]= 0 
