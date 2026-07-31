class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            print(left,right)
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return list(filter(lambda x: nums[x] == target, [left,right,mid]))[0]
            if nums[left] > nums[right]:
                if nums[left] < nums[mid]:
                    if nums[left] < target < nums[mid]:
                        right = mid
                    else:
                        left = mid
                else: 
                    if nums[mid] < target < nums[right]:
                        left = mid
                    else:
                        right = mid
            else:
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        
        return -1

                
            