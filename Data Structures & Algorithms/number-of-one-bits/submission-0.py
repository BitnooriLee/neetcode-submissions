class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        #add last bit
        #bit shift 
        while n:
            res += n%2
            n = n >> 1

        return res
        