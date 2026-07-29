class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        gridHeight = len(grid)
        gridLength = len(grid[0])

        freshFruit = set()
        rottenFruit = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshFruit.add((i,j))
                elif grid[i][j] == 2:
                    rottenFruit.add((i,j))
        
        time = 0
        while freshFruit:
            buf = set()
            for rotten in rottenFruit:
                for direction in directions:
                    y = rotten[0] + direction[0]
                    x = rotten[1] + direction[1]
                    if not 0 <= y < gridHeight:
                        pass
                    elif not 0 <= x < gridLength:
                        pass
                    else:
                        if (y,x) in freshFruit:
                            freshFruit.remove((y,x))
                            buf.add((y,x))
            
            if len(buf) == 0:
                return -1
            else:
                rottenFruit = rottenFruit.union(buf)
                time += 1
        
        return time

