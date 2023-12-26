class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        dp
        """

        memo = {}
        def calc(start, memo, target):
            
            
            if start == n and target == 0:
                return 1
            if start >= n or target <= 0:
                return 0
            if (start, target) in memo:
                return memo[(start, target)]
            ways = 0
            for i in range(1, k+1):          
                ways = (ways + calc(start+1, memo, target-i)) % (10**9 + 7)
            memo[(start, target)] = ways
            return ways
        return calc(0, memo, target)
