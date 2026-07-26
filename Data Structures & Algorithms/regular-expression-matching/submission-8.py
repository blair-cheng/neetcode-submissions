class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)
        dp = [[False]*(cols+1) for _ in range(rows + 1)]
        # dp[i][j]=True/False: whether s[i:] and p[j:] match

        dp[rows][cols] = True 
        for r in range(rows, -1, -1):
            for c in range(cols -1, -1, -1):
                match = r < rows and (s[r] == p[c] or p[c] ==".")

                if (c + 1) < cols and p[c+1] =="*":
                    dp[r][c] = dp[r][c+2] or (match and dp[r+1][c])
                elif match:
                    dp[r][c] = dp[r+1][c+1]
        return dp[0][0]
