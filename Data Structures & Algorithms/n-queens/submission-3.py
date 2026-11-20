class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        col,posDiag, negDiag = set(), set(), set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (c + r )  in posDiag or (r - c) in negDiag:
                    continue
                board[r][c] = "Q"
                col.add(c); posDiag.add(r + c); negDiag.add(r - c)
                backtrack(r + 1)
                board[r][c] = "."
                col.remove(c); posDiag.remove(r + c); negDiag.remove(r - c)

        backtrack(0)
        return res


