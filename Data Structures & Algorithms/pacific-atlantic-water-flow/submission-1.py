class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pa = set()
        at = set() 
        m,n = len(heights), len(heights[0])
        output = [] 
        move = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(i,j,visit, prev):
            if i<0 or i>= m or j<0 or j>=n or (i,j) in visit or heights[i][j] < prev:
                return 
            visit.add((i,j))
            for di,dj in move:
                dfs(i+di,j+dj, visit, heights[i][j])
        
        for j in range(n):
            #pa.add([0,j])
            #at.add([m-1,j])
            dfs(0,j, pa,heights[0][j])
            dfs(m-1,j, at,heights[m-1][j])
            #dfs call 
        for i in range(m):
            #pa.add([i,0])
            #at.add([i,n-1])
            dfs(i,0, pa,heights[i][0])
            dfs(i,n-1, at,heights[i][n-1])
                    
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pa and (i,j) in at:
                    output.append([i,j])
        return output 