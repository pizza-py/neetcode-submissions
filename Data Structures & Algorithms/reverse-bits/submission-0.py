class Solution:
    def reverseBits(self, n: int) -> int:
        numberStack = []
        num = n
        while num:
            numberStack.append(num%2)
            num = num//2
        
        while len(numberStack) < 32:
            numberStack.append(0)

        res = 0
        mult = 1
        while numberStack:
            digit = numberStack.pop()
            res += digit*mult
            mult *= 2
        return res

            
        