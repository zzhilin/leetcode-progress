class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
            
        
        dp = {}
        """
        1,3,5,8,10,15,20
        """
        # dp[right][diff] = len sub
        
        for right in range(len(nums)):
            for left in range(0,right):
                diff = nums[right] - nums[left]
                dp[(right,diff)] = dp.get((left, diff),1)+1

        return max(dp.values())
                