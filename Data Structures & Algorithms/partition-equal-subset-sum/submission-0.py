class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        dp = set()
        for number in nums:
            for thing in dp.copy():
                dp.add(number+thing)
            dp.add(number)
        
        return total//2 in dp
        