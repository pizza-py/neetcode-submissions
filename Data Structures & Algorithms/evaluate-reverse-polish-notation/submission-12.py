class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : lambda x,y: x+y, 
            "*" : lambda x,y: x*y, 
            "-" : lambda x,y: x-y, 
            "/" : lambda x,y: int(x/y), 
        }
        numbers = []
        for symbol in tokens:
            print(symbol)
            print(numbers)
            if symbol.isnumeric() or (symbol[1:len(symbol)].isnumeric()):
                numbers.append(symbol)
            else:
                n1 = int(numbers.pop())
                n2 = int(numbers.pop())
                numbers.append(str(operators[symbol](n2,n1)))
            print(numbers)
        return int(numbers[0])
        