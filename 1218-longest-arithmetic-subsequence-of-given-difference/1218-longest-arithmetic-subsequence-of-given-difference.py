class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp[i] longest len subsequence ending at arr[i]
        # find arr[j] that arr[j] - arr[i] = diff -> dp[i] = dp[j]+1 else dp[i] = 1
        # dp[0] = 1
        dp = {}
        max_len = 0
        
        for num in arr:
            if num-difference in dp:
                dp[num] = dp[num-difference] + 1
            else:
                dp[num] = 1
            max_len = max(max_len, dp[num])
        return max_len
                
        
        
        
        
        
        