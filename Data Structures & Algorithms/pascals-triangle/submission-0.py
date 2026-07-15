class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalsTriangle = []
        def triangle(self, n):
            if n == 1:
                pascalsTriangle.append([1])
                return [1]
            else:
                array = [1]
                prev = triangle(self,n-1)
                for i in range(1,n-1):
                    print("n = " + str(n))
                    print("i = " + str(i))
                    print(prev)
                    print("")
                    array.append(prev[i-1] + prev[i])
                array.append(1)
                pascalsTriangle.append(array)
                return array
        triangle(self, numRows)
        return pascalsTriangle
        