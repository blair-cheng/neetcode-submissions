class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])

        for start, end in intervals:
            # not overlap
            if not res or start > res[-1][1]:
                res.append([start,end])                    
            # overlap
            else:
                res[-1][1] = max(res[-1][1],end)
        return res




































        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # if has interval
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # if no interval    
            else:
                output.append([start, end])

        return output
                