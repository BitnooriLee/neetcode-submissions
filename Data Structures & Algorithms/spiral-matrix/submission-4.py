class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])

        top, bottom = 0, m-1
        left, right = 0, n-1
        res = []
        
        while(top<=bottom and left <= right):
        #top left right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+= 1    
        #right top bottom 
            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1 

        #bottom right left 
            if top <= bottom: #top -1 해줬으니 
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -=1 

        #left bottom top #right -1 해줬으니 
            if left<=right:
                for j in range(bottom,top-1,-1):
                    res.append(matrix[j][left])
                left += 1 

        return res

            
        
        