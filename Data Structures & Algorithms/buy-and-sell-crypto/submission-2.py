class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle case where list has one element
        if len(prices) == 1:
            return 0

        left = 0
        right = 1

        lowest_price = 1000000000
        best_profit = 0

        while left < len(prices)-1:
            # Track lowest price as we sweep from left to right
            lowest_price = min(lowest_price, prices[left])

            # Use lowest price as buy, check against current day
            cur_profit = prices[right] - lowest_price
            if cur_profit > best_profit:
                best_profit = cur_profit

            left += 1
            right += 1
        
        return best_profit
