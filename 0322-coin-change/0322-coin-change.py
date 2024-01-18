class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Empty Coins Array -> return -1
        amount is 0 -> return 0
        single type of coin -> check if amount can be divided by coin if no then return -1
        duplicate coin value
        
        subproblem: find min coin needed for certain amount
        combination(curr value of )
        
        case [2],3
        '''

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for c in coins:
            for x in range(c, amount+1):
                dp[x] = min(dp[x], dp[x-c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

