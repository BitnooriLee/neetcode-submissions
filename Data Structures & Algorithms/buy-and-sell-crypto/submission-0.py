class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0 
        min_price = prices[0]

        for price in prices:
            #sell
            prof = max(prof, price-min_price)
            #buy
            min_price = min(min_price,price)

        return prof

        