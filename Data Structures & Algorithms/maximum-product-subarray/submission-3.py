class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1
        for num in nums:
            if num == 0:
                curMin = 1
                curMax = 1
            else:
                temp = curMax
                curMax = max(num, num * curMax, num*curMin)
                curMin = min(num, num*temp, num*curMin)
                res = max(curMax, res)
        return res


        
        