class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        unvisited = []
        gridHeight = len(grid)
        gridLength = len(grid[0])
        
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
                    dfs(i+1, j)
                    dfs(i-1, j)
                    dfs(i, j+1)
                    dfs(i, j-1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    numberOfIslands += 1
        return numberOfIslands
        