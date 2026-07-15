class Solution:
    def climbStairs(self, n: int) -> int:
        ptr1 = 1
        ptr2 = 2
        if n <= 2:
            return n
        for i in range(0,n-2):
            temp = ptr2
            ptr2 = ptr1 + ptr2
            ptr1 = temp
        return ptr2
        