class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            total = 0
            num = i
            while num > 0:
                total += num %2
                num = num // 2
            res.append(total)
        return res
        