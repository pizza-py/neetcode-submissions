class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxP = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                maxP = max([maxP, prices[i]-prices[buy]])
        return maxP
