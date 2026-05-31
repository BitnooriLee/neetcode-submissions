class Solution:
    def hammingWeight(self, n: int) -> int: 
        cnt = 0 
        while(n):
            n = n&(n-1) # 가장 오른쪽 1 사라짐;;;;
            cnt+=1 
        return cnt
        
        