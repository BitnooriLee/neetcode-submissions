class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r = 0, m-1 
        tr = 0 
        while(l<=r):
            m = (r-l)//2 + l
            if target < matrix[m][0]:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m +1 
            else:
                break
        else:
            return False #while else 

        lc, rc = 0, n-1
        while(lc<=rc):
            mid = (rc-lc)//2 + lc
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                lc = mid+1
            else:
                rc = mid-1 

        return False

        