class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[i,j] for i in [-1,1,0] for j in [-1,1,0] if abs(i+j)==1]
        boardHeight = len(board)
        boardLength = len(board[0])
        seen = set()
        cur = []
        def dfs(space):
            if (not 0 <= space[0] < boardHeight) or (not 0 <= space[1] < boardLength):
                return False
            else:
                if board[space[0]][space[1]] == "X":
                    return True
                elif board[space[0]][space[1]] == "O":
                    seen.add(tuple(space))
                    res = True
                    for direction in directions:
                        nextSpace = [space[0] + direction[0], space[1]+ direction[1]]
                        if tuple(nextSpace) not in seen:
                            res &= dfs(nextSpace)

                    cur.append(space)
                    return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i,j) not in seen:
                    cur = []
                    if dfs([i,j]):
                        for space in cur:
                            board[space[0]][space[1]] = "X"

