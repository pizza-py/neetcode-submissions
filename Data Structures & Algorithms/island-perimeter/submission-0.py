class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        perimeter = 0
        gridHeight = len(grid)
        gridLength = len(grid[0])
        for i in range(gridHeight):
            for j in range(gridLength):
                if grid[i][j] == 1:
                    total = 0
                    for direction in directions:
                        if not 0 <= i+direction[0] < gridHeight or not 0 <= j+direction[1] < gridLength:
                            total += 1
                            continue
                        if grid[i+direction[0]][j+direction[1]] == 0:
                            total+=1
                    perimeter += total
        
        return perimeter
        