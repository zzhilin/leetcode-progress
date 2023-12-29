class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10 ** 9 + 7
        dp = [[[0 for _ in range(k+1)] for j in range(m+1)] for _ in range(n+1)]
        
        for num in range(len(dp[0])):
            dp[n][num][0] = 1
        
        for i in range(n-1, -1, -1):
            for max_so_far in range(m, -1, -1):
                for remain in range(k+1):
                    res = (max_so_far * dp[i+1][max_so_far][remain]) % MOD
                    if remain > 0:
                        for x in range(max_so_far+1, m+1):
                            res = (res + dp[i+1][x][remain-1]) % MOD
                    dp[i][max_so_far][remain] = res
                    
        return dp[0][0][k]