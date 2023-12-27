class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def find(ind, total, dp):
            if ind == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (ind, total) in dp:
                return dp[(ind, total)]
            
            # curr symbol is -
            subtract_curr = find(ind+1, total-nums[ind], dp)
            
            # +
            take = find(ind+1, total+nums[ind], dp)
            
            dp[(ind, total)] = subtract_curr + take
            return dp[(ind, total)]
        
        dp = {}
        # print(dp)
        return find(0,0,dp)