class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        calls = 0
        def helper(a,b):
            if (a,b) in cache:
                return cache[(a,b)]
            if a == 1 or b == 1:
                cache[(a,b)] = 1
                return 1
            else:
                sum1 = 0
                sum2 = 0 
                if (a-1,b) in cache:
                    sum1 = cache[(a-1,b)]
                else:
                    sum1 = helper(a-1,b)
                if (a,b-1) in cache:   
                    sum2 = cache[(a,b-1)]
                else:
                    sum2 = helper(a,b-1)
                
                cache[(a,b)] = sum1+sum2
                return sum1 + sum2
        return helper(m,n)
        




        