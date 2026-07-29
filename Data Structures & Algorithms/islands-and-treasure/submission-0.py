class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        gridHeight = len(grid)
        gridLength = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue = [(i,j), "+"]
                    visited = set()
                    dist = 0
                    while len(queue) > 1:
                        print(queue)
                        cur = queue.pop(0)
                        print("cur =",cur)
                        print("")
                        if cur == "+":
                            dist += 1
                            queue.append("+")
                        elif not 0 <= cur[0] < gridHeight:
                            pass
                        elif not 0 <= cur[1] < gridLength:
                            pass
                        else:
                            y = cur[0]
                            x = cur[1]
                            if grid[y][x] <= 0 and (y,x) != (i,j):
                                pass
                            elif (y,x) not in visited:
                                grid[y][x] = min(dist, grid[y][x])
                                visited.add((y,x))
                                queue.append((y+1,x))
                                queue.append((y-1,x))
                                queue.append((y,x+1))
                                queue.append((y,x-1))

        