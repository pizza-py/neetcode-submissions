class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        addition = sum(range(0,len(nums)+1))
        return addition - sum(nums)