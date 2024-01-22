class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[0 for _ in range(n+1)] for _ in range(goal+1)]
        # print(dp)
        dp[0][0] = 1 # number of lists with length i containing j unique songs
        # number of ways we can make a playlist of length goal exactly n unique songs
        for i in range(1, goal+1):
            for j in range(1, min(i, n)+1):
                # add new song
                dp[i][j] = dp[i-1][j-1] * (n-j+1) % MOD
                if j > k:
                    # replay
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % MOD
        return dp[goal][n]