class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()

        def bfs(r,c):
            while q:
                r,c = q.popleft()
                neighbors = [
                    (r+1,c),(r-1,c),(r,c+1),(r,c-1)
                ]
                for nr,nc in neighbors:
                    if ( 0<=nr<rows 
                    and 0<= nc < cols
                    and grid[nr][nc] > grid[r][c] + 1
                    ):
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        bfs(r,c)

            
































