class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]

            if cash - price > hold:
                hold = cash - price

            if hold + price - fee > cash:
                cash = hold + price - fee

        return cash