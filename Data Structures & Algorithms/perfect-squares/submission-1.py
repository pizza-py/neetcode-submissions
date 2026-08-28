class Solution:
    def numSquares(self, n: int) -> int:
        dp = [99]*(n+1)
        i = 1
        squares = []
        while i*i < n+1:
            squares.append(i*i)
            dp[(i*i)] =1
            i += 1
        
        print(squares)
        for i in range(1,n+1):
            for j in squares:
                if j > i:
                    break
                dp[i] = min(dp[i], dp[j] + dp[i-j])
        return dp[-1]