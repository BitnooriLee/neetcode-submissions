class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        d = [(0,1), (1,0), (-1,0), (0,-1)]
        m,n = len(heights), len(heights[0])
        p = deque()
        a = deque()
        p_set = set()
        a_set = set()

        for i in range(m):
            p.append([i,0])
            a.append([i,n-1])
        for j in range(n):
            p.append([0,j])
            a.append([m-1,j])

        def dfs(dq,visited):
            while dq:
                x,y = dq.popleft()
                visited.add((x,y))
                for dx,dy in d:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                        if heights[x][y] <= heights[nx][ny]:
                            dq.append([nx,ny])
                            visited.add((nx,ny))
        dfs(p,p_set)
        dfs(a,a_set)

        for i in p_set:
            if i in a_set:
                res.append(i)

        return res 


        

        
        