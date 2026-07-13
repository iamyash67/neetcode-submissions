"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        minheap = []
        heapq.heappush(minheap,intervals[0].end)
        for cur in intervals[1:]:
            if cur.start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, cur.end)
        return len(minheap)
