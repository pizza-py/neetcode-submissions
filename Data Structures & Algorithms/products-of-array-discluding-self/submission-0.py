class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[n-i-1] = suffix[n-i] * nums[n-i-1]

        result = []
        for i in range(n):
            if i == 0:
                result.append(suffix[i+1])
            elif i == n-1:
                result.append(prefix[n-1-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])
        return result 