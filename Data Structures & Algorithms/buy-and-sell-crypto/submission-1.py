class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx, sell_idx = 0, 1
        max_profit = 0
        while sell_idx < len(prices):
            if prices[sell_idx] > prices[buy_idx]:
                max_profit = max(max_profit, prices[sell_idx] - prices[buy_idx])
            else:
                buy_idx = sell_idx

            sell_idx += 1
        
        return max_profit