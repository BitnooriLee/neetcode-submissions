class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0 

        for _ in range(32):
            output=2*output + (n&1)
            n>>=1
        return output


        