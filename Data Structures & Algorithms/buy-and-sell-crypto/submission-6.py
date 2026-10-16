class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        maxprofit = 0

        buy = 0
        sell = 1

        while sell < L:
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprofit = max(profit, maxprofit)
            else:
                buy = sell
            sell += 1
        return maxprofit

        