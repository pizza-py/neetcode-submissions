class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = dict()
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        largestLucky = -1
        for key in count:
            if count[key] == key:
                largestLucky = max(largestLucky, key)
        return largestLucky
        