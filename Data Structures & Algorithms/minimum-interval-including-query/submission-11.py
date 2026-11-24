class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries) 
        intervals.sort()
        nqueries = []
        hq = []
        
        for index,q in enumerate(queries):
            nqueries.append((q,index))
        nqueries.sort()

        i = 0
        for q, index in nqueries:
            while i < len(intervals) and intervals[i][0]<=q:
                left, right = intervals[i]
                heapq.heappush(hq, (right - left + 1, right))
                i += 1
            while hq and hq[0][1] < q:
                heapq.heappop(hq)
            if hq:
                res[index] = hq[0][0]

        return res
