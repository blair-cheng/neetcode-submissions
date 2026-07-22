class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals[[0,1], ... ]
        # queries[i] = length of the shortest interval i
        # return -1 or [index of smallest interval according to queries[i] ]
        # sort start 
        # minHeap{key =right_i - left_i + 1| value = (i, right_i ) }

        intervals.sort()
        minHeap = []
        res, i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0]<= q :
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]

