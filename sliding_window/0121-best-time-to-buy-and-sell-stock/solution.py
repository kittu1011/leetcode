class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        curr_min = prices[0]
        for x in prices:
            curr_min = min(x,curr_min)
            result = max(result, x - curr_min)
        return result