class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        gridHeight = len(grid)
        gridLength = len(grid[0])
        
        islands = [0]

        def dfs(i,j):
            total = 0
            if not (0 <= i < gridHeight) or not (0 <= j < gridLength):
                return total

            if grid[i][j] == 0:
                return total

            grid[i][j] = 0
            total = 1

            total += dfs(i+1, j)
            total += dfs(i-1, j)
            total += dfs(i, j+1)
            total += dfs(i, j-1)
            return total


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    islands.append(dfs(i,j))
        return max(islands)