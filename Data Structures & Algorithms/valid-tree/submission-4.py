class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        edges2 = list(map(lambda x: [x[1]] + [x[0]], edges ))
        adjMap = {}
        for edge in edges+edges2:
            if edge[0] in adjMap:
                adjMap[edge[0]].append(edge[1])
            else:
                adjMap[edge[0]] = [edge[1]]

        visited = set()
        takenEdges = set()

        def dfs(node):
            res = True
            visited.add(node)
            for adj in adjMap[node]:
                if (node, adj) not in takenEdges:
                    takenEdges.add((adj, node))
                    if adj in visited:
                        return False
                    print(node, adj)
                    res &= dfs(adj)
            return res
        
        return dfs(list(adjMap.keys())[0]) and len(visited) == len(adjMap.keys())
