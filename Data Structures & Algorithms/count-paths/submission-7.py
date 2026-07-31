import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.comb(m+n-2,n-1))

        




        