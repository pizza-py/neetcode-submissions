class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        res = []
        for i in range(len(temperatures)):
            j = i
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                else:
                    j += 1
            if j == len(temperatures):
                res.append(0)
        return res

