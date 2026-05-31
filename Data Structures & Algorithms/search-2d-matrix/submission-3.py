class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        lm, rm = 0, m-1 
        
        while(lm<=rm):
            mm = lm + (rm-lm)//2
            if matrix[mm][0] == target:
                return True
            elif matrix[mm][0] > target:
                rm = mm -1 
            else:
                lm = mm +1 
        if lm < 0:
            return False 
        row = lm -1 
        ln,rn = 0, n-1
        while(ln<=rn):
            mn = ln + (rn-ln)//2
            if matrix[row][mn] == target:
                return True
            elif matrix[row][mn] > target:
                rn = mn -1 
            else:
                ln = mn +1 
        return False
