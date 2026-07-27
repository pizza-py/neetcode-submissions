class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def isPalindrome(p):
            if len(p) == 0:
                return False
            ptr1 = 0
            ptr2 = len(p)-1
            while ptr1 < ptr2:
                if p[ptr1] != p[ptr2]:
                    print(p, "is not palindrome")
                    return False
                ptr1 += 1
                ptr2 -=1
            print(p, "is palindrome")
            return True

        def dfs(i,string):
            if i == len(s)-1:
                if isPalindrome(string):
                    print("Adding cur = ", cur)
                    cur.append(string)
                    res.append(cur.copy())
                    cur.pop()
                    return
                else:
                    print("cur = ", cur, "did not qualify")
                    return
            else:
                if isPalindrome(string):
                    print("Current string: ", string)
                    cur.append(string)
                    dfs(i+1, s[i+1])
                    cur.pop()
                    dfs(i+1, string + s[i+1])
                    return
                else:
                    print("Current string: ", string)
                    dfs(i+1, string + s[i+1])
                    return
        
        dfs(0,s[0])
        return res


        