class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for a in nums:
            if a not in newList:
                newList.append(a)
        if len(newList) != len(nums):
            return True
        else:
            return False