class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        boardHeight = len(board)
        boardLength = len(board[0])

        cur = []
        def dfs(space, string):
            if not string:
                return True
            elif not 0 <= space[0] < boardHeight or not 0 <= space[1] < boardLength:
                return False
            else:
                if board[space[0]][space[1]] == string[0]:
                    res = False
                    for direction in directions:
                        nextSpace = [space[0] + direction[0], space[1] + direction[1]]
                        cur.append(space)
                        if nextSpace not in cur:
                            res |= dfs(nextSpace, string[1:])
                        cur.pop()
                    return res
                else:
                    return False
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs([i,j], word):
                        return True
        return False
        