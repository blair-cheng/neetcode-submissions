class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = set()
        minH = [[0,0]]
        res = 0
        for i in range(len(points)):
            a, b = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                c, d = points[j]
                cost = abs(a-c)+ abs(b-d)
                adj[i].append((cost,j))

        while len(visit)<len(points):
            cost, point = heapq.heappop(minH)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for c, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minH,[c,nei])

        return res
