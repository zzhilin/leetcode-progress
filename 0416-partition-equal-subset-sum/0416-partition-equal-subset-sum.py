class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def isSubSumEqual(nums, idx, target, dp):
            # basecase
            for i in range(len(nums)):
                dp[i][0] = True
                
            for i in range(1, len(nums)):
                for t in range(1, target+1):
                    # choose / no
                    no = dp[i-1][t] # whether it is possible to achieve the current target sum t by excluding the current element nums[i] from the subset.
                    is_curr_taken = False # whether it is possible to achieve the current target sum by including the current element nums[i] in the subset.
                    # we can include curr into subset sum
                    if nums[i] <= t:
                        is_curr_taken = dp[i-1][t-nums[i]]
                    dp[i][t] = is_curr_taken or no
                    
            return dp[len(dp)-1][len(dp[0])-1]
                        
                
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        # dp[i][j] is wwhether we can get subset sum j using first i elements in nums
        dp = [[False for i in range(target+1)] for j in range(len(nums))]
        return isSubSumEqual(nums, len(nums), target, dp)