class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        resList = sorted(stones)[::-1]

        while (len(resList) > 1):
            if resList[0] == resList[1]:
                resList.pop(0)
                resList.pop(0)
            else:
                resList[0] = resList[0] - resList[1]
                resList.pop(1)
            resList = sorted(resList)[::-1]
            print(resList)
        
        if len(resList) == 1:
            return resList[0]
        else:
            return 0
            
        