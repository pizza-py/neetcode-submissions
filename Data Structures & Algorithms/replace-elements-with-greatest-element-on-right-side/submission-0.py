class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        return [max(arr[i+1:]) for i in range(len(arr)-1)] + [-1]
        