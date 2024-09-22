class Solution(object):
    def should_merge(self, first_interval, second_interval):
        if (first_interval[1] < second_interval[0]):
            return False
        return True

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals.sort()
        intervals.sort(key = lambda i : i[0])
        print(intervals)
        res = []
        recent_interval = intervals[0]
        for i in range(len(intervals) - 1):
            merged = self.should_merge(recent_interval, intervals[i+1])
            if (merged):
                recent_interval = [min(recent_interval[0], intervals[i+1][0]), max(recent_interval[1], intervals[i+1][1])]
                # print("recent_interval", recent_interval)
            else:
                res.append(recent_interval)
                recent_interval = intervals[i+1]
        res.append(recent_interval)
        return res

    
        
