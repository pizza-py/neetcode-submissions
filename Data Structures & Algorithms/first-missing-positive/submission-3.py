class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        ptr = len(nums)+1
        smallest = ptr
        while ptr>=1:
            print(ptr)
            if ptr not in setOfNums:
                smallest = ptr
            ptr -=1 
        return smallest
        
        