class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        newList = []
        for i in range(len(nums)):
            newList.append(nums[(i-k) % (len(nums))])
        for i in range(len(newList)):
            nums[i] = newList[i]