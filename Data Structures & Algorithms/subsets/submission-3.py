class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        elif len(nums) == 1:
            return [nums,[]]
        else:
            subset1 = self.subsets(nums[1:])
            subset2 = []
            for subset in subset1:
                subset2.append(subset + [nums[0]])
            return subset1 + subset2
