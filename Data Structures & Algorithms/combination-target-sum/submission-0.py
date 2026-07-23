class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        collection = []

        def dfs(total, i):
            if i >= len(nums):
                return
            if total == target:
                res.append(collection.copy())
                return
            elif total > target:
                return
            
            collection.append(nums[i])
            dfs(total + nums[i], i)

            collection.pop()
            dfs(total, i+1)
        
        dfs(0,0)
        return res