class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(x):
            t = 0 
            for pile in piles:
                t += (pile + x -1) // x #ceil 

            if t <= h:
                return True
            else:
                return False 

        l,r = 1, max(piles)
        while(l<r):
            mid = r + (l-r)//2 
            if finish(mid):
                r = mid 
            else:
                l = mid +1 
        
        return l 
                