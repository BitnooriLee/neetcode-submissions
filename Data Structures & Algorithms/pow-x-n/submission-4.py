class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0 
        if n == 1:
            return x 

        if n < 1: 
            reverse = True 
            n = -n 
        else:
            reverse = False
            
        res = 1 
        base = x
        while(n>0):
            if n%2 == 1:
                res *= base
            
            base = base*base
            n = n//2
        return res if not reverse else 1/res
            
        