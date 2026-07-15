class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisStack = []
        openBrackets = {"(","{","["}
        bracketMap = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }
        for i in range(len(s)):
            cur = s[i]
            if cur in openBrackets:
                parenthesisStack.append(cur)
            else:
                if len(parenthesisStack) == 0:
                    return False
                if cur != bracketMap[parenthesisStack.pop()]:
                    return False
        
        if len(parenthesisStack) != 0:
            return False
        else:
            return True