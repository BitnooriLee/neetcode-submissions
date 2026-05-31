import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def total_hour(k):
            t = 0 
            for p in piles:
                t += math.ceil(p/k)
            return t 

        l,r = 1, max(piles)+1

        while(l<r):
            m = l + (r-l)//2
            if total_hour(m) <= h:
                r=m
            else:
                l=m+1 

        return l
        