class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        Neg = False
        if x < 0:
            x = -x 
            Neg = True
        
        output = 0
        while(x):
            if output > MAX//10 or (output == MAX//10 and x%10 > 7):
                return 0
            output *= 10
            cur = x%10
            x = x//10 
            output+= cur 
            
        return output if not Neg else -output



            
        