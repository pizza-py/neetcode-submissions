class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        else:
            rest = self.subsets(nums[1:len(nums)])
            rest2 = []
            for elem in rest:
                tmp = elem.copy()
                tmp.append(nums[0])
                rest2.append(tmp)
            return rest + rest2