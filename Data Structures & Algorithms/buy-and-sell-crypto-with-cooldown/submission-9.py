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
                profit_if_wait = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, profit_if_wait)

            else:
                sell = dfs(i+2, not buying) + prices[i]
                profit_if_wait = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, profit_if_wait)
            return dp[(i, buying)]
        return dfs(0, True)