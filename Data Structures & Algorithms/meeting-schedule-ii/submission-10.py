"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h=[-1]
        nroom=0
        intervals=sorted(intervals, key=lambda x: x.start)

        for i in intervals:
            if i.start < h[0]:
                heapq.heappush(h, i.end)
            else:
                heapq.heappop(h)
                heapq.heappush(h, i.end)
            nroom=max(nroom, len(h))
            print(i.start, i.end, nroom)
        return nroom