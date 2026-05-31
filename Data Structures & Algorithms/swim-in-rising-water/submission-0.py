class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        best = [[float("inf")]*n for _ in range(n)]
        best[0][0] = grid[0][0]        
        minh = [(grid[0][0],0,0)] #cost, r,c 
        move = [(0,1),(1,0),(-1,0),(0,-1)]

        while(minh):
            cost, r, c = heapq.heappop(minh)
            if r == n-1 and c == n-1:
                return best[r][c]
            if cost != best[r][c]:
                continue
            for dr,dc in move:
                if 0<= r+dr<n and 0<= c+dc<n:
                    new = max(cost, grid[r+dr][c+dc])
                    if new < best[r+dr][c+dc]:
                        best[r+dr][c+dc] = new
                        heapq.heappush(minh, (new, r+dr, c+dc))
            
        
       

        
        
        
            
        