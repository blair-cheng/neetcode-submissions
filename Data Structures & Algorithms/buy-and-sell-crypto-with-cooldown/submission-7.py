class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buy or sell
        # if buy: index + 1
        # if sell: index + 2
        # dp = from day[i:], the max profit if buy/sell (True/False)
        dp = {} # key = (i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying ) in dp:
                return dp[(i,buying)]
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)