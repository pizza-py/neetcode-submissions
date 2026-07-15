class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[i] + nums[len(nums)-j-1] == target:
                    return [i,len(nums)-j-1]
        return False