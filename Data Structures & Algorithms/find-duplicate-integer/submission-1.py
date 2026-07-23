class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        return max(count, key=count.get)
        