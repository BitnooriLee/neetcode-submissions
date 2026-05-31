class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = len(grid) # squre 
        move = [(0,1), (1,0), (0,-1), (-1,0)]
        visit = set()
        minh = [(grid[0][0], (0,0))]
        visit.add((0,0))

        while minh:
            if minh[0][1] == (l-1,l-1):
                return minh[0][0]
            d, (i,j) = heapq.heappop(minh)
                
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<=ni<l and 0<=nj<l and (ni,nj) not in visit:
                    visit.add((ni,nj))
                    heapq.heappush(minh, (max(grid[ni][nj],d), (ni,nj)))
                    

    