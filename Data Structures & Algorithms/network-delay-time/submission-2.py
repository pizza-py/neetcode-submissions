import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = {}
        distMap = {}
        for i in range(1,n+1):
            distMap[i] = bool(not i==k) * 999999
        for time in times:
            adjMap[time[0]] = adjMap.get(time[0],[]) + [[time[1],time[2]]]
        
        queue = [[0,k]]
        visited = set()
        
        while queue:
            cur = heapq.heappop(queue)
            if cur[1] in visited:
                continue
            visited.add(cur[1])
            if cur[1] in adjMap:
                for val in adjMap[cur[1]]:
                    temp = distMap[val[0]]
                    distMap[val[0]] = min(distMap[val[0]] ,val[1] + cur[0])
                    if val[0] not in visited and distMap[val[0]] < temp:
                        heapq.heappush(queue,[distMap[val[0]], val[0]])
        
        maxTime = max(distMap.values())
        if maxTime == 999999:
            return -1
        else: 
            return maxTime





