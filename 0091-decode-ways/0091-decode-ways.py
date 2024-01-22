class Solution:
    def numDecodings(self, s: str) -> int:
        # find number of ways to decode
        # dp
        # topdown
        
        # 121 127 012 102
        # start with 0-> terminate
        # find number of ways at curr index
        # curr number is more than 26 -> terminate
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            memo[i] = res
            return res
        
        memo = {len(s): 1} # default num of ways at n
        return dfs(0)