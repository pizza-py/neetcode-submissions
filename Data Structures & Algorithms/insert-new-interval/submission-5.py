class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #linear search 

        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        

        res = []
        i = 0
        insertedStart = False
        while not insertedStart and i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                if intervals[i][1] < newInterval[0]:
                    res.append(intervals[i])
                else:
                    insertedStart = True
                    res.append([intervals[i][0], "?"])
            else:
                insertedStart = True
                res.append([newInterval[0],"?"])
            i += 1
        
        i-=1
        print(res, i)
        

        insertedEnd = False
        while not insertedEnd and i < len(intervals):
            if intervals[i][0] <= newInterval[1]:
                if intervals[i][1] < newInterval[1]:
                    pass
                else:
                    insertedEnd = True
                    res[-1][1] = intervals[i][1]
            else:
                insertedEnd = True
                res[-1][1] = newInterval[1]
                i-=1
            i+= 1
        
        while i<len(intervals):
            res.append(intervals[i])
            i+=1

        if res[-1][1] == "?":
            res[-1][1] = newInterval[1]
        
        return res


            



        