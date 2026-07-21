class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlapping
            if start >= prevEnd:
                prevEnd = end
            # overlapping, remove/ignore the larger end interval
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
