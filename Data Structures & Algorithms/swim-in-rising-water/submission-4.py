class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        visit = set()
        
        n = len(grid)
        
        minh = [(grid[0][0], (0,0))]
        visit.add((0,0))
        while(minh):
            if minh[0][1] == (n-1,n-1):
                return minh[0][0]
            d, (r,c) = heapq.heappop(minh)
            

            for dr,dc in move:
                if 0<= r+dr <n and 0<= c+dc <n and (r+dr, c+dc) not in visit:
                    visit.add((r+dr, c+dc))
                    heapq.heappush(minh, (max(grid[r+dr][c+dc],d), (r+dr,c+dc)))
                        
            

    
