class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        climb(steps, n) = climb(steps+1, n) or climb(steps+2, n)
        base curr = n
        curr > n
        '''
        def climb(curr_steps, dest_steps, memo):
            if curr_steps == dest_steps:
                return 1
            if curr_steps > dest_steps:
                return 0
            if curr_steps in memo:
                return memo[curr_steps]
            memo[curr_steps] = climb(curr_steps+1, dest_steps, memo) + climb(curr_steps+2, dest_steps, memo)
            return memo[curr_steps]
        
        return climb(0, n, {})