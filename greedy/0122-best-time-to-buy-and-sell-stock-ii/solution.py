# greedy solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            result += max(0,prices[i]-prices[i-1])
        return result
# 2d-dp solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_bought = 0 # stock is currently held
        last_sold = 0 # no stock is currently held
        for x in reversed(prices):
            temp = last_sold
            last_sold = max(last_sold, last_bought - x) # buying a stock
            last_bought = max(last_bought, temp + x) # selling a stock

        return last_sold
