class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set(map(str, range(1,27)))
        dp = [0]*len(s)

        if s[0] == "0":
            return 0
        
        dp[0] = 1
        i = 1
        while i < len(s):
            c1 = s[i-1]
            c2 = s[i]
            group = c1 + c2
            print(c1,c2,group)

            canGetFrom1 = c2 in valid
            canGetFrom2 = group in valid
            print(canGetFrom1, canGetFrom2)
            if canGetFrom1 and canGetFrom2:
                if i == 1:
                    dp[i] = dp[0] + 1
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            elif canGetFrom1:
                dp[i] = dp[i-1]
            elif canGetFrom2:
                if i == 1:
                    dp[i] = 1
                else:
                    dp[i] = dp[i-2]
            else:
                return 0
            i+=1
        print(dp)
        return dp[-1]
            






            