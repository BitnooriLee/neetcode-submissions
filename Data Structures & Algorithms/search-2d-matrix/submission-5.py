class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        cl,cr = 0, len(matrix)-1
        while(cl<=cr):
            m = cl + (cr-cl)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                cl += 1
            else:
                cr -= 1
        rl,rr = 0, len(matrix[0])-1
        while(rl<=rr):
            m = rl + (rr-rl)//2
            if matrix[cr][m] == target:
                return True
            elif matrix[cr][m] < target:
                rl += 1
            else:
                rr -= 1
        return False