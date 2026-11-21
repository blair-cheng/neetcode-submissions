class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def backtrack(r,c,n):
            if not (0<=r<rows and 0<=c < cols) or (r,c) in path or board[r][c]!= word[n]:
                return False
            if n == len(word)-1:
                return True
            path.add((r,c))

            
            found = (
                backtrack(r+1, c, n+1) or 
                backtrack(r-1, c, n+1) or 
                backtrack(r, c-1, n+1) or 
                backtrack(r, c+1, n+1) 
            )
            path.remove((r,c))
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False

        