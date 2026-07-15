class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1,temp2 = sorted([ord(char) for char in s]),sorted(ord(char) for char in t)
        return temp1 == temp2
