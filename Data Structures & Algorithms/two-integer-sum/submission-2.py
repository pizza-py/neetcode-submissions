class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverseMap = {}
        for i in range(len(nums)):
            inverseMap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in inverseMap and inverseMap[target-nums[i]] != i :
                return [i, inverseMap[target-nums[i]]]
        