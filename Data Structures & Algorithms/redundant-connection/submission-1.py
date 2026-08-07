class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap = dict()
        for edge in edges:
            if edge[0] in adjMap:
                adjMap[edge[0]].append(edge[1])
            else:
                adjMap[edge[0]] = [edge[1]]
            if edge[1] in adjMap:
                adjMap[edge[1]].append(edge[0])
            else:
                adjMap[edge[1]] = [edge[0]]
        print(adjMap)
        
        visited = set()
        cycleSet = set()
        def dfs(i,parent):
            print(i)
            visited.add(i)
            for adj in adjMap[i]:
                if adj != parent:
                    if adj in visited:
                        cycleSet.add((i, adj))
                        print((i,adj))
                        return True
                    else:
                        res = dfs(adj, i)
                        if not res:
                            pass
                        else:
                            if i not in cycleSet:
                                cycleSet.add((i, adj))
                                print((i,adj))
                                return True
                            else:
                                return False


            return False
        
        dfs(edges[0][0], None)
        
        for i in range(len(edges)-1,-1,-1):
            print(tuple(edges[i]))
            print(reversed(tuple(edges[i])))
            if tuple(edges[i]) in cycleSet or tuple(reversed(edges[i])) in cycleSet:
                return edges[i]
