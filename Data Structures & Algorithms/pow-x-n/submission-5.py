class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 1:
            return x 

        if n < 0:
            Neg = True
            n = -n 
        else:
            Neg = False

        
        res = 1 
        base = x 
        while(n>0):
            if n%2 == 1:
                res *= base
            base *= base
            n //=2  
        return res if not Neg else 1/res

        