class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        output = []
        for num in range(n+1):
            tmp = 0
            for _ in range(32):
                if num&1:
                    tmp+=1
                num >>= 1
            output.append(tmp)
                
        return output
                


        