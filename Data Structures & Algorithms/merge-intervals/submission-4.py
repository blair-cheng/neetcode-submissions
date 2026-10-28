class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])

        pre_start, pre_end = intervals[0]

        for i in range(1,len(intervals)):
            start, end = intervals[i]

            # not overlap
            if start > pre_end:
                res.append([pre_start,pre_end])
                pre_start, pre_end = start, end
                    
            # overlap
            else:
                pre_start = min(pre_start,start)
                pre_end = max(pre_end, end)
        res.append([pre_start, pre_end])
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
                