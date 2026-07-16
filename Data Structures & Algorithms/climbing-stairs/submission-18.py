class Solution:
    def climbStairs(self, n: int) -> int:
        things = dict()
        def dfs(num):
            print(things)
            if num <= 2: 
                things[num] = num
                return num
            else:
                stair1 = 0
                if num-1 in things:
                    stair1 = things[num-1]
                else:
                    stair1 = dfs(num-1)
                stair2 = 0
                if num-2 in things:
                    stair2 = things[num-2]
                else:
                    stair2 = dfs(num-2)
                things[num] = stair1+stair2
                return things[num]
        return dfs(n)

        