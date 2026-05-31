class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = len(grid)
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        visit = set()
        minh = [(grid[0][0],(0,0))]
        visit.add((0,0))
        while minh:
            if minh[0][1] == (l-1,l-1):
                return minh[0][0]

            d, (i,j) = heapq.heappop(minh)
            visit.add((i,j))
            for di,dj in move:
                if 0<=i+di<l and 0<=j+dj<l and (i+di, j+dj) not in visit:
                    heapq.heappush(minh, (max(grid[i+di][j+dj],d), (i+di, j+dj)))

                