class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        def total_h(speed):
            th = 0 
            for p in piles:
                th += math.ceil(p/speed)
            return th

        while(l<r):
            m = (r-l)//2 + l
            if total_h(m) > h:
                l = m + 1 
            else:
                r = m 
        return l


        

        