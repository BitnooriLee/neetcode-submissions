class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        q = set()
        move = [(1,0),(0,1),(-1,0),(0,-1)]
        que_p = deque() 
        que_q = deque() 
        m, n = len(heights), len(heights[0])

        for j in range(0,n):
            que_p.append((0,j))
            p.add((0,j))
        for i in range(0,m):
            que_p.append((i,0))
            p.add((i,0))
        for j in range(0,n):
            que_q.append((m-1,j))
            q.add((m-1,j))
        for i in range(0,m):
            que_q.append((i,n-1))
            q.add((i,n-1))


        def bfs(que,s):
            while que:
                i,j = que.popleft()
                for di, dj in move:
                    ni,nj = i+di, j+dj
                    if ni < 0 or ni >=m or nj <0 or nj >= n:
                        continue 
                    if (ni,nj) in s:
                        continue
                    if heights[i][j] <= heights[ni][nj]:
                        s.add((ni,nj))
                        que.append((ni,nj))
        
        bfs(que_p, p)
        bfs(que_q, q)

        res = []
        for (i,j) in p:
            if (i,j) in q:
                res.append([i,j])

        return res


            

        