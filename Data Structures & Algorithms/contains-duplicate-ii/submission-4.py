class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ptr = 0
        if k > len(nums):
            return True
        while ptr+k <= len(nums):
            segment = nums[ptr:ptr+k+1]
            segmentSet = set(segment)
            if len(segmentSet) != len(segment):
                return True
            ptr += 1
        return False
        