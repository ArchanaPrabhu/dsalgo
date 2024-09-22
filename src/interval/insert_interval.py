class Solution(object):
    def should_merge(self, first_interval, second_interval):
        if (first_interval[1] <= second_interval[0]):
            return False
        return True

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i : i[0])
        count_list = [0 for _ in range(len(intervals))]
        print(intervals)
        res = []
        ans = 0
        recent_interval = intervals[0]
        for i in range(len(intervals) - 1):
            mergeable = self.should_merge(recent_interval, intervals[i+1])
            if (mergeable):
                # which ever interval finishes first, we retain them
                if (recent_interval[1] > intervals[i+1][1]):
                    recent_interval = intervals[i+1]
                ans += 1
            else:
                recent_interval = intervals[i+1]
        
        return ans

    
        

        
