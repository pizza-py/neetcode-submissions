class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        def permuteCurrent(self,current,numsCopy):
            if len(numsCopy) == 1:
                return [[current]]
            temp = numsCopy.copy()
            print(current)
            print(temp)
            print("")
            temp.remove(current)
            prev = permuteCurrent(self,temp[0],temp)
            newThing = []
            for i in range(len(prev)):
                permutation = prev[i]
                for i in range(len(permutation)+1):
                    permCopy = permutation.copy()
                    permCopy.insert(i,current)
                    newThing.append(permCopy)
            return newThing
        return permuteCurrent(self,nums[0],nums.copy())