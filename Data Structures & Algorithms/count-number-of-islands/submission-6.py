class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        gridHeight = len(grid)
        gridLength = len(grid[0])
        
        numberOfIslands = 0

        def dfs(i,j):
            if not (0 <= i < gridHeight) or not (0 <= j < gridLength):
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    numberOfIslands += 1
        return numberOfIslands
        