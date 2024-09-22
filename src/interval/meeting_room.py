"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def check_for_conflict(self, first, second):
        if (first.end <= second.start):
            return False
        return True

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if (len(intervals) == 0):
            return True
        recent_interval = intervals[0]

        for i in range(len(intervals) - 1):
            is_conflicting = self.check_for_conflict(recent_interval, intervals[i+1])
            if (is_conflicting):
                return False
            elif (recent_interval.end < intervals[i+1].end):
                    recent_interval = intervals[i+1]
        return True
