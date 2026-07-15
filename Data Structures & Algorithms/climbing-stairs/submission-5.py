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
        if n-1 not in self.things:
            self.things[n-1] = self.climbStairs(n-1)
        if n-2 not in self.things:
            self.things[n-2] = self.climbStairs(n-2)
        self.things[n] = self.things[n-1] + self.things[n-2]
        return self.things[n]

        