class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        p = deque()
        q = deque()
        vp = set()
        vq = set()

        for i in range(m):
            p.append([i,0])
            q.append([i,n-1])

        for j in range(n):
            p.append([0,j])
            q.append([m-1,j])


        def dfs(dq,visited):
            while dq:
                x,y = dq.popleft()
                visited.add((x,y))
                for dx,dy in move:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                        if heights[x][y] <= heights[nx][ny]:
                            dq.append([nx,ny])
                            visited.add((nx,ny))
        dfs(p,vp)
        dfs(q,vq)
        res = []
        
        for a in vp:
            if a in vq:
                res.append(a)

        return res                

            