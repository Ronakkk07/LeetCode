class Solution:
    def maxProfit(self, prices):
        # TC -O(N), O(1)
        minimum = prices[0]
        profit = 0
        for i in range(len(prices)):
            cost = prices[i] - minimum
            profit = max(profit, cost)
            minimum = min(minimum, prices[i])
        return profit