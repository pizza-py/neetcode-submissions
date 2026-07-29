class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        cur = []
        res = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
            else:
                cur.append(nums[i])
                dfs(i+1)
                cur.pop()
                dfs(i+1)

        dfs(0)
        
        finalRes = []

        for subset in res:
            if subset not in finalRes:
                finalRes.append(subset)
        return finalRes

        