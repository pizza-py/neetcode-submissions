import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = 0
        while left <= right:
            mid = int((left + right)/2)
            total = sum(map(lambda n: math.ceil(n/mid), piles))
            if total > h:
                left = mid+1
            else: 
                if mid == 1:
                    return 1
                total2 = sum(map(lambda n: math.ceil(n/(mid-1)), piles))
                if total2 > h:
                    return mid
                else:
                    right = mid-1
        return mid

