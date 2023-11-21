class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            # compare nums[i] with each previous element nums[j] 
            for j in range(i):
            # If nums[i] is greater than nums[j]
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                # check if we can increase subsequence at dp[i] to dp[j]+1
                    dp[i] = dp[j]+1
        return max(dp)
            