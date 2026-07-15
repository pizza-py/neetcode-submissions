class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            cur1 = s[i]
            ptr1 = i-1
            ptr2 = i+1
            isPalindrome = True
            while isPalindrome and (ptr1 >= 0) and (ptr2 < len(s)):
                left = s[ptr1]
                right = s[ptr2]
                if left == right:
                    cur1 = left + cur1 + right
                    ptr1 -= 1
                    ptr2 +=1
                else:
                    isPalindrome = False


            cur2 = ""
            ptr1 = i-1
            ptr2 = i
            isPalindrome = True
            while isPalindrome and (ptr1 >= 0) and (ptr2 < len(s)):
                left = s[ptr1]
                right = s[ptr2]
                if left == right:
                    cur2 = left + cur2 + right
                    ptr1 -= 1
                    ptr2 +=1
                else:
                    isPalindrome = False
            longest = max([longest, cur1, cur2], key=len)
        return longest
