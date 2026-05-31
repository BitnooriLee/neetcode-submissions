class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(mat):
            m = len(mat)
            for i in range(m):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i],mat[i][j]

        transpose(matrix)

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        