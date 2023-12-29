class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        def dp(ind, max_so_far, remain_cnt):
            #base
            if ind == n:
                if remain_cnt == 0:
                    return 1
                return 0
            if remain_cnt < 0:
                return 0
            if memo[ind][max_so_far][remain_cnt] != -1:
                return memo[ind][max_so_far][remain_cnt]
            
            res = 0
            # fill 0 to k-1 elements (1,max)
            for num in range(1, max_so_far+1):
                res = (res + dp(ind+1, max_so_far, remain_cnt)) % MOD
            # max+1, m
            for num in range(max_so_far+1, m+1):
                res = (res + dp(ind+1, num, remain_cnt-1)) % MOD
            memo[ind][max_so_far][remain_cnt] = res
            return res
        MOD = 10 ** 9 + 7
        memo = [[[-1 for _ in range(k+1)] for j in range(m+1)] for _ in range(n)]
        return dp(0,0,k)