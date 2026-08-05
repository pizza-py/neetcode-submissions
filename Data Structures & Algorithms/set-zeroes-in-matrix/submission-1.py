class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrixHeight = len(matrix)
        matrixLength = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    direct = 1
                    while i+direct < matrixHeight:
                        if matrix[i+direct][j] != 0:
                            matrix[i+direct][j] = "x"
                        direct += 1
                    direct = -1
                    while i+direct >= 0:
                        if matrix[i+direct][j] != 0:
                            matrix[i+direct][j] = "x"
                        direct -= 1
                    direct = 1
                    while j+direct < matrixLength:
                        if matrix[i][j+direct] != 0:
                            matrix[i][j+direct] = "x"
                        direct += 1
                    direct = -1
                    while j+direct >=0:
                        if matrix[i][j+direct] != 0:
                            matrix[i][j+direct] = "x"
                        direct -= 1
        
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "x":
                    matrix[i][j] = 0

        
        