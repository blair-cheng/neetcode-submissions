class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotton = collections.deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs():
            nonlocal fresh
            minutes = 0

            while rotton and fresh > 0:
                size = len(rotton)
                for _ in range(size):
                    r,c = rotton.popleft()
                    neighbors = [
                        [r,c+1],[r,c-1],[r+1,c],[r-1,c]
                    ]
                    for nr,nc in neighbors:
                        if ( 0<=nr< rows  
                        and 0<= nc< cols
                        and grid[nr][nc] == 1):
                            grid[nr][nc] =2
                            fresh -= 1
                            rotton.append((nr,nc))
                minutes += 1
            return minutes

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotton.append((r,c))
                elif grid[r][c] ==1:
                    fresh += 1

        minutes = bfs()

        return minutes if fresh ==0 else -1




