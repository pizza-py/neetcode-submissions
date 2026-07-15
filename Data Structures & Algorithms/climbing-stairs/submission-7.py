class Solution:
    things = {
        1 : 1,
        2 : 2
    }
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            stairs1 = 0
            stairs2 = 0
            if n-1 in self.things:
                stairs1 = self.things[n-1]
            else:
                stairs1 = self.climbStairs(n-1)
                self.things[n-1] = stairs1
            if n-2 in self.things:
                stairs2 = self.things[n-2]
            else:
                stairs2 = self.climbStairs(n-2)
                self.things[n-2] = stairs2
            return stairs1 + stairs2
        