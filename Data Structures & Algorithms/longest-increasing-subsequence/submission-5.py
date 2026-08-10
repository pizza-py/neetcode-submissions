class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i == len(nums)-1:
                cache[i] = 1
                return cache[i]
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    numberForJ = 0
                    if j in cache:
                        numberForJ = cache[j]
                    else:
                        numberForJ = dfs(j)
                
                    if i in cache:
                        cache[i] = max(numberForJ+1, cache[i])
                    else:
                        cache[i] = 1+numberForJ

            if i not in cache:
                cache[i] = 1
            
            return cache[i]
                


        for i in range(len(nums)):
            dfs(i)
        
        return max(cache.values())


            


        