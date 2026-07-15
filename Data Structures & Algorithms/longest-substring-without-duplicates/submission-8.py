class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        current = []
        start = 0
        if len(s) == 0:
            return 0
        current.append(s[start])
        for i in range(1, len(s)):
            if s[i] not in current:
                current.append(s[i])
            else:
                while s[i] in current:
                    current.pop(0)
                current.append(s[i])
            longest = max(longest,len(current))
            print(current)
        return longest