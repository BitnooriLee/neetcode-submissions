class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        MAX = 0x7fffffff
        while(b!=0):
            sum_wo_carry = (a^b)&mask 
            carry = ((a&b)<<1)&mask
            a = sum_wo_carry
            b = carry 

        return a if a <= MAX else ~(a^mask)



        
        
        