class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        # dp[i] will store a dictionary where the key is the common difference
        # and the value is the count of arithmetic subsequences ending at index i
        dp = [defaultdict(int) for _ in range(length)]
        total_count = 0
        
        for i in range(length):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_at_j = dp[j][diff]
                count_at_i = dp[i][diff]
            
                # Update the count at i by adding count at j plus one for the new subsequence
                dp[i][diff] = count_at_i + count_at_j + 1
                # update total
                total_count += count_at_j
            
        
        return total_count