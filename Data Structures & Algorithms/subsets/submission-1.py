class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnList = []
        n = len(nums)
        def generate(self, arr, i):
            if i == n-1:
                print("First pass at end: i = "+ str(i) + ", arr ="+ str(arr))
                returnList.append(arr.copy())
                arr.append(nums[i])
                print("Second pass at end: i = "+ str(i) + ", arr ="+ str(arr))
                returnList.append(arr.copy())
            else:
                print("First pass not at end: i = "+ str(i) + ", arr ="+ str(arr))
                generate(self, arr.copy(), i+1)
                arr.append(nums[i])
                print("Second pass not at end: i = "+ str(i) + ", arr ="+ str(arr))
                generate(self, arr.copy(), i+1)
        generate(self, [], 0)
        return returnList
            