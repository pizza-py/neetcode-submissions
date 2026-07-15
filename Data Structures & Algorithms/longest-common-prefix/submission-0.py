class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in range(len(strs)):
            newLongest = ""
            n = 0
            while (n < len(longest) and (n < len(strs[i])) and (longest[n] == strs[i][n])):
                newLongest += longest[n]
                n += 1
            longest = newLongest
        return longest