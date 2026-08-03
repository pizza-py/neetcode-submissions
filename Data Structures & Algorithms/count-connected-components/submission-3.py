class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = dict()
        for edge in edges:
            if edge[0] not in adjMap:
                adjMap[edge[0]] = []
            adjMap[edge[0]].append(edge[1])

            if edge[1] not in adjMap:
                adjMap[edge[1]] = []
            adjMap[edge[1]].append(edge[0])

        unvisited = set(adjMap)
        def dfs(node):
            unvisited.remove(node)
            for thing in adjMap[node]:
                if thing in unvisited:
                    dfs(thing)
        
        res = 0
        while unvisited:
            res += 1
            cur = list(unvisited)[0]
            dfs(cur)
        return res + n - len(adjMap)


        