class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        unvisited = []
        gridHeight = len(grid)
        gridLength = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    unvisited.append((i,j))
        
        numberOfIslands = 0
        visited = set()

        def dfs(i,j):
            if not (0 <= i < gridHeight):
                return
            elif not (0 <= j < gridLength):
                return
            else:
                if grid[i][j] == "0":
                    return
                elif grid[i][j] == "1":
                    if (i,j) in visited:
                        return
                    visited.add((i,j))
                    unvisited.remove((i,j))
                    dfs(i+1, j)
                    dfs(i-1, j)
                    dfs(i, j+1)
                    dfs(i, j-1)

        while unvisited:
            dfs(unvisited[0][0], unvisited[0][1])
            numberOfIslands += 1
        return numberOfIslands
        