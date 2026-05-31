class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l = len(nums)
        a =[1] + nums + [1]
        dp = [[0]*(l+2) for _ in range(l+2)]

        for length in range(1, l+1):
            for i in range(1, l-length+2): # i...j 
                j = i + length -1
                best = 0

                for k in range(i,j+1):
                    best = max(best, dp[i][k-1] + a[i-1]*a[k]*a[j+1]+ dp[k+1][j])
                dp[i][j] = best 

        return dp[1][l]

        