class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1 
        if n == 0:
            return 1 
        elif n < 0:
            x = 1/x

        for _ in range(abs(n)):
            output *= x 


        return output
            
        