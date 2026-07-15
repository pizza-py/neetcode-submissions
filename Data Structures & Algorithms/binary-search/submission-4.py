class Solution:
    import math
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = math.floor((left+right)/2)
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            elif target == nums[middle]:
                return middle
        return -1


        