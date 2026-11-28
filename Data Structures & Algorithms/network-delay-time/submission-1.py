class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))
        minH = [[0,k]]
        visit = set()

        while minH:
            w1, u = heapq.heappop(minH)
            if u in visit:
                continue
            visit.add(u)
            t = w1

            for v, w in edges[u]:
                if v not in visit:
                    heapq.heappush(minH,[w1+w,v])
        return -1 if len(visit)< n else t





