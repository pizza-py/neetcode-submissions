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
            print("Added "+ str(n-1) + " to things")
            self.things[n-1] = self.climbStairs(n-1)
            print(self.things)
            print("")
        if n-2 not in self.things:
            print("Added "+ str(n-2) + " to things")
            self.things[n-2] = self.climbStairs(n-2)
            print(self.things)
            print("")
        print(n-1 in self.things)
        print(n-2 in self.things)
        self.things[n] = self.things[n-1] + self.things[n-2]
        return self.things[n]

        