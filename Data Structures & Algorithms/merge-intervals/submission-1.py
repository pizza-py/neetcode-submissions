class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            resCur = res[-1]

            if resCur[0] <= cur[0] <= resCur[1]:
                resCur[1] = max(cur[1], resCur[1])
            else:
                res.append(cur)
        
        return res
            
