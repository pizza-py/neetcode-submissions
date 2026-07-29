class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        thing = sorted(nums)
        maximum = 1
        length = 1
        ptr = 0
        if len(nums) == 0:
            return 0
        while ptr < len(thing)-1:
            if thing[ptr+1] - thing[ptr] == 0:
                pass
            elif thing[ptr+1] - thing[ptr] == 1:
                length += 1
                maximum = max(length,maximum)
            else:
                length = 1
            ptr += 1 
        
        return maximum
        