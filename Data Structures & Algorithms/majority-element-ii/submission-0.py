class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        return list(filter(lambda x: count[x] > len(nums)//3, count))
        