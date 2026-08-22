class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0:0, 1:1, 2:1}
        def helper(k):
            n1 = 0
            n2 = 0
            n3 = 0

            if k in cache:
                return cache[k]
            if k-1 in cache:
                n1 = cache[k-1]
            else:
                n1 = helper(k-1)
            if k-2 in cache:
                n2 = cache[k-2]
            else:
                n2 = helper(k-2)
            if k-3 in cache:
                n3 = cache[k-3]
            else:
                n3 = helper(k-3)
            
            cache[k] = n1 + n2 + n3

            return cache[k]
        
        return helper(n)
        