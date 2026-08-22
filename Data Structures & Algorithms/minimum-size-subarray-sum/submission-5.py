class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = len(nums)+1
        left = 0
        right = 0
        cur = nums[0]
        while left < len(nums) and right < len(nums):
            if cur >= target:
                best = min(best, right-left+1)
                cur -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    cur += nums[right]
            
            if left > right:
                right += 1
                if right < len(nums):
                    cur += nums[right]
        return best if best != len(nums)+1 else 0
            
        