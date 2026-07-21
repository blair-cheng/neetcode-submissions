class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        # dp[i] = number of 1s in i's binary representation

        for i in range(1, n + 1):
            dp[i] = dp[i>>1] + (i & 1)

        return dp