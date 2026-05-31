class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix)


        for i in range(m//2):
            for j in range(n):
                matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]

        for i in range(m):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
            
        