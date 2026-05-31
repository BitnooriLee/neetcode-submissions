class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0 :
            return 1 
        if n == 1:
            return x 

        if n < 0:
            x = 1/x
            n = -n

        res = 1.0
        base = x  
        while(n>0):
            if n%2 == 1:
                res = res*base
            
            base = base*base
            n = n//2 
        
        return res
                
