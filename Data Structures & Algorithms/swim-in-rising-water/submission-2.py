class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = []
        visit = set()
        n = len(grid)
        minH = [[grid[0][0],0,0]]
        visit.add((0,0))
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == n-1 and c == n-1:
                return t

            discover = ((r+1,c), (r-1,c),(r,c+1), (r,c-1))
            for dr,dc in discover:
                if (dr,dc) not in visit and 0<=dr<n and 0<=dc < n:
                    heapq.heappush(minH,[max(t,grid[dr][dc]),dr,dc])
                    visit.add((dr,dc))
            

