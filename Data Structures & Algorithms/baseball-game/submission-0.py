class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        stack = {
            "x" : lambda x: scores.append(int(x)),
            "+" : lambda :  scores.append(scores[-1] + scores[-2]),
            "D" : lambda : scores.append(scores[-1] * 2),
            "C" : lambda : scores.pop()
        }
        
        for char in operations:
            if char not in ["+","D","C"]:
                stack["x"](char)
            else:
                stack[char]()
        return sum(scores)
