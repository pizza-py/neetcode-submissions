class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        best = 1
        while right < len(s):
            window = s[left:right+1]
            mostFrequent = max(map(window.count, window))
            windowSize = right-left+1
            if (windowSize - mostFrequent) <= k:
                best = max(windowSize, best)
                right += 1
            else:
                left += 1
        return best

