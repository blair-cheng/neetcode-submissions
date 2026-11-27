class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0],0,0]]
        visit = set()
        visit.add((0,0))
        n = len(grid)
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == n-1 and c == n-1:
                return t
            discover = ((r+1,c),(r-1,c), (r,c+1),(r,c-1))

            for dr,dc in discover:
                if 0<=dr<n and  0<=dc<n and (dr,dc) not in visit:
                    heapq.heappush(minH,[max(t,grid[dr][dc]),dr,dc])
                    visit.add((dr,dc))
            

