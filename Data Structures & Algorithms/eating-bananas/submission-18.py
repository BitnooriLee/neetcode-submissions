class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return False

        def canEat(n):
            total = 0 
            for pile in piles:
                total+= math.ceil(pile/n)
            return True if total <= h else False

        l,r = 1, max(piles)+1

        while(l<r):
            m = l + (r-l)//2
            if canEat(m):
                r = m 
            else:
                l = m + 1 
        return l 


        