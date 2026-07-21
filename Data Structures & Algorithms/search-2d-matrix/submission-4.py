class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        mid = 0
        while left <= right:
            mid = int((left + right)/2)
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                right = mid-1
            else:
                if mid+1 < len(matrix) and target >= matrix[mid+1][0]:
                    left = mid+1
                else:
                    left = mid
                    right = mid-1
        row = matrix[mid]
        print(row)
        left = 0
        right = len(row)-1
        while left <= right:
            mid = int((left + right)/2)
            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid-1
            else:
                left = mid+1
        return False


        