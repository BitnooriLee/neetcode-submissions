class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = False
        if n < 0:
            neg = True
            n = -n 

        cur = x 
        res = 1 
        while(n):
            if n%2 == 1:
                res *= cur
            cur *= cur 
            n = n//2
        
        return res if not neg else 1/res
            

            
        
        