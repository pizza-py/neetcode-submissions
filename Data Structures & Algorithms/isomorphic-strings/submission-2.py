class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myMap = dict()
        unavailables = set()
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in myMap:
                if myMap[c1] != c2:
                    return False
                else:
                    pass
            else:
                if c2 in unavailables:
                    return False
                myMap[c1] = c2
                unavailables.add(c2)
        return True
        
        