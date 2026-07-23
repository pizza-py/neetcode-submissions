class Solution:
    def isPalindrome(self, s: str) -> bool:
        filterAlphanumeric = lambda x: (0 <= ord(x) - ord("a") <= 25) or (0 <= ord(x)-ord("A") <= 25) or (0 <= ord(x)-ord("0")<=9)
        return list(filter(filterAlphanumeric, s[::-1].lower())) == list(filter(filterAlphanumeric,s.lower()))
        