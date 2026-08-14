class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        cur = []
        res = []
        def dfs(i, total):
            if total < 0:
                return
            elif total == 0:
                res.append(cur.copy())
                return

            if i >= len(candidates):
                return
            else:
                cur.append(candidates[i])
                dfs(i+1, total - cur[-1])
                thing = cur.pop()
                while i < len(candidates) and candidates[i] == thing:
                    i+=1
                dfs(i, total)

        dfs(0,target)
        return res


        
            
        