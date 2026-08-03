class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        cache = {}
        maxLength = len(max(wordDict, key=len))
        
        def helper(string):
            cur = ""
            possibles = []
            res = False

            if string == "":
                return True

            for i in range(maxLength):
                if i < len(string):
                    cur += string[i]
                    if cur in wordSet:
                        possibles.append(i)
                else:
                    if cur in wordSet:
                        return True
                    else:
                        break
            for thing in possibles:
                if string[thing+1:] not in cache:
                    cache[string[thing+1:]] = helper(string[thing+1:])
                res |= cache[string[thing+1:]]
            
            return res
        
        return helper(s)
            

            
            
                


        