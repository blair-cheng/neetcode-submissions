class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = set()
        res = 0
        minH = [[0,0]]

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append([cost,j])
        
        while len(visit) < len(points):
            cost, point = heapq.heappop(minH)
            if point in visit:
                continue
            visit.add(point)
            res += cost
            for nei in adj[point]:
                neic, neip = nei
                if neip not in visit:
                    heapq.heappush(minH,[neic,neip])
        return res
