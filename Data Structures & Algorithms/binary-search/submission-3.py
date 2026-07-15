class Solution:
    import math
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        considered = nums
        while True: 
            middle = int((math.ceil(len(considered))/2))     
            if len(considered) == 1:
                if target != considered[0]:
                    return -1
                else:
                    return index
            elif len(considered) == 0:
                return -1

            print(middle)
            print(considered)
            if target < considered[middle]:
                considered = considered[0:middle]
            elif target > considered[middle]:
                considered = considered[middle+1:len(considered)]
                index = index + middle + 1
            elif target == considered[middle]:
                return index + middle


        