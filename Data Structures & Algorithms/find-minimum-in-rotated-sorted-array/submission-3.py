class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left] < nums[(left-1) % len(nums)]:
                return nums[left]
            mid = (right + left) // 2
            print(left,mid,right)
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
        
        return nums[(left+1) %len(nums)]
            
        