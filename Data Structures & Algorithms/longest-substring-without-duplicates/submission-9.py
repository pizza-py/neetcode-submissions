class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        best = 0
        seenQueue = []
        while right < len(s):
            if s[right] in seenQueue:
                left += 1
                seenQueue.pop(0)
            else:
                seenQueue.append(s[right])
                best = max(best, right - left + 1)
                right += 1
        return best