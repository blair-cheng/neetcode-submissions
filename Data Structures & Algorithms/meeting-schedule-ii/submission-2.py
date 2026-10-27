"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ends = []
        starts = sorted(intervals, key = lambda x: x.start )

        for meeting in starts:
            if ends and ends[0] <= meeting.start:
                heapq.heappop(ends)
            heapq.heappush(ends, meeting.end) 

        return len(ends)












