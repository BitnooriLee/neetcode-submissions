class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        def totalTime(k):
            s = 0 
            for banana in piles:
                s += banana//k if banana%k == 0 else banana//k + 1 
            return s 

        while(l<=r):
            m = l + (r - l)//2
            if totalTime(m) <= h:
                r = m - 1 
            else:
                l = m + 1
    
        return l
    

        