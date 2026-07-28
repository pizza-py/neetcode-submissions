class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute force O(n^2)
        maximum = nums[0]
        curSum = 0
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(nums):
            curSum += nums[ptr2]
            maximum = max(maximum, curSum)
            if curSum < 0:
                ptr1 = ptr2+1
                curSum = 0
            ptr2 += 1
            
        
        return maximum

            
        