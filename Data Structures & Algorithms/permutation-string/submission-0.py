class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1 = 0
        length = len(s1)
        while p1+length <= len(s2):
            substring = sorted(s2[p1:p1+length])
            if sorted(s1) == substring:
                return True
            p1 += 1
        return False