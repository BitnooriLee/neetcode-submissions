class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0 
        for sell in prices:
            if sell > buy:
                res = max(res, sell-buy)
            else:
                buy = sell # 현재 가격이 산 가격보다 싸다면 
        return res 

        