class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = 0
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            cur = intervals[i]
            resCur = res[-1]
            if cur[0] < resCur[1]:
                resCur[1] = min(resCur[1], cur[1])
                result += 1
            else:
                res.append(cur)
        
        print(res)
        return result
        