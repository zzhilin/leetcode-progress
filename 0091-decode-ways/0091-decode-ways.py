class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: end at curr digit, how many ways to decode / how many combinations
        # if s[i] == 0, return 0 (cannot decode)
        # basically if cannot decode, dp[i] = dp[i-1] * 1 if s[i] != 0
        # if curr and prev can decode, dp[i] = dp[i] + dp[i-2]*1
        
        dp = {len(s): 1}
        def dfs(i):
            
            # good: already cached curr s[i] or we are at the end
            if i in dp:
                return dp[i]
            # bad base case: s[i] is 0
            if s[i] == "0":
                return 0
            
            # here solve our sub problem: s[i] is between 1 to 9, and we take only single digit
            res = dfs(i+1)
            # case we can take 2: next is in bound and valid (< 27)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
                
            dp[i] = res
            return res
        
        # how many ways we can decode s start at 0
        return dfs(0)