class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 1:
            return x
            
        neg = False
        if n < 0:
            neg = True
            n = -n


        res = 1
        cur = x 

        while(n>0):
            if n%2 == 1:
                res *= cur
            cur *= cur
            n = n//2 

        return res if not neg else 1/res
        
        