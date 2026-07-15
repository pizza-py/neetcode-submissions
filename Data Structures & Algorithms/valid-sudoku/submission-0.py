class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        squares = []
        rows = []
        columns = [[],[],[],[],[],[],[],[],[]]
        for i in range(len(board)):
            rows.append([])
            for j in range(len(board[i])):
                rows[i].append(board[i][j])
                columns[j].append(board[i][j])


        for j in range(0,9,3):
            for i in range(0,9,3):
                squares.append([
                    rows[j][i], rows[j][i+1], rows[j][i+2], rows[j+1][i], rows[j+1][i+1], rows[j+1][i+2], rows[j+2][i], rows[j+2][i+1], rows[j+2][i+2]
                ])

        stuff = [rows,columns,squares]      
        for typ in stuff:            
            for thing in typ:
                seen = []
                for item in thing:
                    if (item not in seen) and (item != "."):
                        seen.append(item)
                    elif item == ".":
                        pass
                    else:
                        valid = False
        return valid