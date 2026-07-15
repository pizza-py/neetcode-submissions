class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = []
        for i in range(2*len(nums)):
            new.append(nums[i%len(nums)])
        return new