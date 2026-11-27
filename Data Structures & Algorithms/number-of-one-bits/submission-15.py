class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for _ in range(32):
            if n&1: #bit and 0000001
                cnt+=1 # 오른쪽 한칸밀기 
            n >>= 1

        return cnt
        