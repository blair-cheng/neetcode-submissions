class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        candidateq = []
        qq = []
        intervals.sort()

        for index, query in enumerate(queries):
            heapq.heappush(qq, (query, index))
        
        i = 0
        while qq:
            query, index = heapq.heappop(qq)
            while i < len(intervals) and intervals[i][0]<= query:
                left, right = intervals[i]
                heapq.heappush(candidateq,(right-left + 1, right))
                i += 1
            while candidateq and candidateq[0][1] < query:
                heapq.heappop(candidateq)
            if candidateq:
                res[index] = candidateq[0][0]

        return res
            

        