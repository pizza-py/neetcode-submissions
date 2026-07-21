import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = 0
        while left <= right:
            mid = int((left + right)/2)
            print(mid)
            total = sum(map(lambda n: math.ceil(n/mid), piles))
            if total > h:
                left = mid+1
                mid = mid+1
            else: 
                right = mid-1
        return mid

