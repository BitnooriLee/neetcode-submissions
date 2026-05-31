class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1 
        if n == 0:
            return 1 
        elif n < 0:
            x = 1/x
            n = - n 
        current = x 

        while n > 0:
            if n%2:
                output *= current
            current *= current
            n //= 2 


        return output
            
        