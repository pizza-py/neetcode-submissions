class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        num = n
        while num > 0:
            total += (num % 2)
            num = num // 2
        return total