class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle case where list has one element
        if len(prices) == 1:
            return 0

        profit = 0

        for i in range(0, len(prices)-1):
            # Setup iteration pointers
            left = i
            right = left + 1

            # Initialize the buy value with first element in list
            buy_price = prices[left]

            while right < len(prices):
                # If the sell_diff is higher than the current best sell_diff, replace profit
                sell_diff = prices[right] - prices[left]
                if sell_diff > profit:
                    profit = sell_diff

                right += 1
            left += 1

        print(profit)
        return profit
        