class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        res = [-1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            res[i] = maximum
            maximum = max(maximum, arr[i])
        return res

        