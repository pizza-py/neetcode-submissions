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
                    return False
                ptr1 += 1
                ptr2 -=1
            return True

        def dfs(i,string):
            if i == len(s)-1:
                if isPalindrome(string):
                    cur.append(string)
                    res.append(cur.copy())
                    cur.pop()
                    return
                else:
                    return
            else:
                if isPalindrome(string):
                    cur.append(string)
                    dfs(i+1, s[i+1])
                    cur.pop()
                    dfs(i+1, string + s[i+1])
                    return
                else:
                    dfs(i+1, string + s[i+1])
                    return
        
        dfs(0,s[0])
        return res


        