class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                inserted = True
                intervals.insert(i, newInterval)
        
        if not inserted:
            intervals.append(newInterval)
        
        res = [intervals[0]]
        for i in range(len(intervals)):
            cur = intervals[i]
            resCur = res[-1]
            if resCur[0] <= cur[0] <= resCur[1]:
                resCur[1] = max(resCur[1], cur[1])
            else:
                res.append(cur)
        
        return res



            



        