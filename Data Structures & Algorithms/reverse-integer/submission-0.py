class Solution:
    def reverse(self, x: int) -> int:
        stringx = str(x)
        res = 0
        if x < 0:
            stringx = stringx[1:]
            res = -int(stringx[::-1])
        else:
            res = int(stringx[::-1])
        if not -2147483647 <= res <= 2147483647:
            return 0
        else:
            return res

        