class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i,price in enumerate(prices[:-1]):
            if (prices[i+1] - price ) > 0:
                profit += (prices[i+1] - price)
        return profit
