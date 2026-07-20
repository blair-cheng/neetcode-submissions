class Solution:
    def numDecodings(self, s: str) -> int:


        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1
        # let dpi be the number of solutions with string s[i:]
        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if (i + 1 < len(s)) and (s[i] == "1" or ((s[i] == "2" and s[i+1] in "0123456"))):
                    dp[i] += dp[i+2]
        return dp[0]
