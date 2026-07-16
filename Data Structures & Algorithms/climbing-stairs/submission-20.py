class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        left, right = 1,2
        for i in range(n-2):
            temp = left+right
            left = right
            right = temp
        return right


        