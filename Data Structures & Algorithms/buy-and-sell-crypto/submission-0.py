class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, buy_price_idx, max_profit = prices[0], 0, 0
        for idx, price in enumerate(prices):
            if price < buy_price:
                buy_price = price
                buy_price_idx = idx
                continue
            elif idx > buy_price_idx and price - buy_price > max_profit:
                max_profit = price - buy_price
        
        return max_profit