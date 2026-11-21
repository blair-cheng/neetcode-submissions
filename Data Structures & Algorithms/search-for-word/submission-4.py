class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def backtrack(i,j,n):
            if i>=rows or i < 0 or j >= cols or j < 0:
                return False
            if  board[i][j] != word[n]:
                return False
            if (i, j) in path:
                return False

            if n == len(word) - 1:
                return True
            path.add((i,j))

            found = (
                backtrack(i+1,j,n+1) or 
                backtrack(i-1,j,n+1) or 
                backtrack(i,j+1,n+1) or 
                backtrack(i,j-1,n+1)
            )
            path.remove((i,j))
            return found
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True

        return False
        

        