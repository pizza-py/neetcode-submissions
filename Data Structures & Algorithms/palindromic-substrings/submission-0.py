class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            ptr1 = i-1
            ptr2 = i+1
            isPalindrome = True
            total += 1
            while isPalindrome and (ptr1 >= 0) and (ptr2 < len(s)):
                left = s[ptr1]
                right = s[ptr2]
                if left == right:
                    ptr1 -= 1
                    ptr2 +=1
                    total += 1
                else:
                    isPalindrome = False


            ptr1 = i-1
            ptr2 = i
            isPalindrome = True
            while isPalindrome and (ptr1 >= 0) and (ptr2 < len(s)):
                left = s[ptr1]
                right = s[ptr2]
                if left == right:
                    total += 1
                    ptr1 -= 1
                    ptr2 +=1
                else:
                    isPalindrome = False
        return total