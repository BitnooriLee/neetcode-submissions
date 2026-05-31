class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        Neg = False
        if x < 0:
            x = -x 
            Neg = True
        
        output = 0
        while(x):
            if not(MIN//10 <= output <= MAX//10):
                return 0
            output *= 10
            cur = x%10
            x = x//10 
            if not(MIN - cur <= output <= MAX - cur):
                return 0
            output+= cur 
            

        return output if not Neg else -output
            
        