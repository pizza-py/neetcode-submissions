import heapq
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
        intervals = sorted(intervals, key=lambda x: x.start)

        rooms = [intervals[0].end]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            earliestFree = rooms[0]
            if interval.start < earliestFree:
                heapq.heappush(rooms, interval.end)
            else:
                heapq.heapreplace(rooms, interval.end)
        
        return len(rooms)
        