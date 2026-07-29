class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(total):
            if total < 0:
                cache[total] = -1
                return -1
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            if total in coins:
                cache[total] = 1
                return cache[total]
            else:
                thing = []
                for coin in coins:
                    thing.append(dfs(total-coin))
                thing = list(filter(lambda x: x!= -1,thing))
                cache[total] = -1 if thing == [] else 1+min(thing)
                return cache[total]

        return dfs(amount)


        