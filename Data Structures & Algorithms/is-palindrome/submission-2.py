class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub("[^a-z0-9]","",s.lower())
        t = "".join([s[len(s)-i-1] for i in range(len(s))])
        print(s)
        print(t)
        return s == t
