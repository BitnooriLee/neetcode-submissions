class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row 
        # binary search 

        #m 
        l,r = 0, len(matrix)-1

        while(l<=r):
            mid = r + (l-r)//2 
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid+1 
            else:
                r = mid -1 
        l = l -1
        ln, rn = 0, len(matrix[0])-1

        while(ln<=rn):
            mid = rn + (ln-rn)//2 
            if matrix[l][mid] == target:
                return True
            elif matrix[l][mid] < target:
                ln = mid+1 
            else:
                rn = mid -1 
        return False

        