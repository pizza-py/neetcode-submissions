class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(totalOpen, currentOpen):
            if currentOpen == 0:
                if totalOpen == n:
                    res.append("".join(cur))
                    return
                else:
                    cur.append("(")
                    dfs(totalOpen+1, currentOpen+1)
                    cur.pop()
            else:
                if totalOpen == n:
                    cur.append(")")
                    dfs(totalOpen, currentOpen-1)
                    cur.pop()
                else:
                    cur.append("(")
                    dfs(totalOpen+1, currentOpen+1)
                    cur.pop()
                    cur.append(")")
                    dfs(totalOpen, currentOpen-1)
                    cur.pop()
            
        dfs(0,0)
        return res

                



                
        