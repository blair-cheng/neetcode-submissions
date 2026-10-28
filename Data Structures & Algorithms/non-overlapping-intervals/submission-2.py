class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals = sorted(intervals, key = lambda x: x[0])

        pre_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < pre_end:
                pre_end = min(end, pre_end)
                res += 1
            else:
                pre_end = end

        return res





