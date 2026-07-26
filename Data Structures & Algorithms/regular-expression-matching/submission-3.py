class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)

        # 1. 创建 (rows + 1) x (cols + 1) 的二维 DP 矩阵
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]

        # 2. Base Case：空字符串与空模式串绝对匹配
        dp[rows][cols] = True

        # 3. 填表：从右下角往左上角推进
        for r in range(rows, -1, -1):
            for c in range(cols - 1, -1, -1):

                # 判断当前单个字符是否匹配（注意 r 不能越界）
                match = r < rows and (s[r] == p[c] or p[c] == ".")

                # 🌟 情况 A：下一个字符是 '*'（乘法修饰符 Quantifier /ˈkwɒntɪfaɪər/）
                if (c + 1) < cols and p[c + 1] == "*":
                    # 选项 1: 当作 0 次（乘以 0）：直接把 p[c] 和 '*' 抹掉，查 dp[r][c + 2]
                    # 选项 2: 当作 >=1 次（乘以 >=1）：要求当前 match 为 True，并让 s 指针下移，查 dp[r + 1][c]
                    dp[r][c] = dp[r][c + 2] or (match and dp[r + 1][c])

                # 🌟 情况 B：普通字符或 '.'
                elif match:
                    dp[r][c] = dp[r + 1][c + 1]

        # 4. 答案就在左上角
        return dp[0][0]