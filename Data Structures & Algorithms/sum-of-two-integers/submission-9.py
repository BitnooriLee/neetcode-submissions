class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffff
        MAX = 0x7fffff

        carry = 0 
        while(b!=0):
            sum_ow_carry = (a^b)&MASK
            carry = ((a&b)<<1)&MASK
            a = sum_ow_carry
            b = carry

        return a if a <= MAX else ~(a^MASK)

        