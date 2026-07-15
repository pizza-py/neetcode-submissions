class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        dp = [0] * (len(cost))
        dp[len(cost)-1] = cost[len(cost)-1]
        dp[len(cost)-2] = cost[len(cost)-2]
        for i in range(len(cost)-3,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        return dp[0]
            