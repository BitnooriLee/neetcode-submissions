class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r = 0, m-1 
        tr = 0 
        while(l<=r):
            if matrix[l][n-1] < target < matrix[r][0]:
                l +=1 
                r -=1
            elif target >= matrix[r][0]:
                tr = r
                break
            else:
                tr = l 
                break

        lc, rc = 0, n-1
        while(lc<=rc):
            mid = (rc-lc)//2 + lc
            if matrix[tr][mid] == target:
                return True
            elif matrix[tr][mid] < target:
                lc = mid+1
            else:
                rc = mid-1 

        return False

        