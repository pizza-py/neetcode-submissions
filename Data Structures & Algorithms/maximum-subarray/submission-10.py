class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Let's quickly remind ourselves of kadane's algorithm

        prefix = 0
        maximum = nums[0]
        
        i = 0
        while i < len(nums):
            num = nums[i]
            prefix += num
            maximum = max(prefix, maximum)
            if prefix < 0:
                prefix = 0
            i += 1
        
        return maximum




        
            
        