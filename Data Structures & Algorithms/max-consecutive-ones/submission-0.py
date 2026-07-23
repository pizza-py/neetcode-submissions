class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0 
        total = 0
        ptr = 0
        while ptr < len(nums):
            if nums[ptr] == 0:
                total = 0
            else:
                total += 1
                maximum = max(maximum, total)
            ptr += 1
        return maximum
        