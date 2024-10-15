class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        min_p = float('inf')

        for i in prices:
            if min_p > i:
                min_p  = i
                continue
            profit = max(profit, i - min_p)

        return profit
        
