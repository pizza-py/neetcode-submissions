class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()
        for i in range(len(strs)):
            sortedString = str(sorted(strs[i]))
            if sortedString in anagramDict.keys():
                anagramDict[sortedString].append(strs[i])
            else:
                anagramDict[sortedString] = [strs[i]]
        
        return list(anagramDict.values())