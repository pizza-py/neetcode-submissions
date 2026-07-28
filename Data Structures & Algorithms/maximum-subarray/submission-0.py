class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute force O(n^2)
        maximum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maximum = max(curSum, maximum)
        return maximum
            
        