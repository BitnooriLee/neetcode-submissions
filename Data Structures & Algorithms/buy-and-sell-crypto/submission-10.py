class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            sell = prices[i]
            if sell > buy:
                res = max(res, sell-buy)
            else:
                buy = sell
            
        return res

#sell r, buy l, l을 업데이트 