class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while cur != 1:
            add = sum(map(lambda x: x**2,map(int, list(str(cur)))))
            if add in seen:
                return False
            else:
                seen.add(add)
                cur = add
        return True