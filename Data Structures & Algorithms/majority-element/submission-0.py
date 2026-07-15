class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        return max(counts.keys(), key = counts.get)