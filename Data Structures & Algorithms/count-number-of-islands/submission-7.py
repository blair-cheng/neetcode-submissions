class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        discovered = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            discovered.add((r,c))

            while q:
                r,c = q.popleft()
                neighbours = [(r+1, c+0),(r-1,c-0),(r+0,c+1),(r+0,c-1)]

                for nr,nc in neighbours:
                    if (0<=nr <rows
                    and 0<=nc < cols
                    and grid[nr][nc] =="1" 
                    and (nr,nc) not in discovered ):
                        q.append((nr,nc))
                        discovered.add((nr,nc)) 


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in discovered:
                    bfs(r,c)
                    res += 1

        return res



