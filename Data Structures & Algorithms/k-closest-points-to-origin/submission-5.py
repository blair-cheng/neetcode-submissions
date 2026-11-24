class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        hq = []

        for p in range(len(points)):
            i, j = points[p]
            distance = (i**2 + j**2)**(1/2) 
            heapq.heappush(hq, (distance,i,j))

        for i in range(k):
            _,i,j = heapq.heappop(hq)
            res.append([i,j])
        return res


        