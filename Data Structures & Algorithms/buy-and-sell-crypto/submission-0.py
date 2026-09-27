class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        best_sell_price = 0

        ans = 0
        for i in range(N - 1, -1, -1):
            price = prices[i]
            best_sell_price = max(price, best_sell_price)

            ans = max(best_sell_price - price, ans)
        
        return ans
        