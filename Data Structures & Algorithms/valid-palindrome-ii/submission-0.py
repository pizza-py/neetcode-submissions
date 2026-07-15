class Solution:
    def palindromeHelper(self, s:str) -> bool:
        ptr1 = 0
        ptr2 = len(s)-1
        while (ptr1 < ptr2):
            if s[ptr1] == s[ptr2]:
                ptr1 +=1
                ptr2 -=1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s)-1
        deleted = False
        while (ptr1 < ptr2):
            if s[ptr1] == s[ptr2]:
                ptr1 +=1
                ptr2 -=1
            else:
                return self.palindromeHelper(s[ptr1:ptr2]) or self.palindromeHelper(s[ptr1+1:ptr2+1])

        return True
        