class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        def finish(x):
            total = 0 
            for i in range(len(piles)):
                total+= math.ceil(piles[i]/mid)
            if total <= h:
                return True
            else:
                return False 

        while(l<r):
            mid = r + (l-r)//2 
            if finish(mid):
                r = mid 
            else:
                l = mid + 1 
        return l 

        # xxxxoooo 