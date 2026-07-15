class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -nums[i]
            i1 = 0
            i2 = len(nums)-1
            while i1 != i2:
                total = nums[i1] + nums[i2]
                if total == target and (len(set([i1,i2,i])) == 3):
                    output.add(tuple(sorted([-target,nums[i1],nums[i2]])))
                    i1 +=1
                    print("added")
                elif total > target:
                    i2 -= 1
                else:
                    i1 +=1
        return list(output)