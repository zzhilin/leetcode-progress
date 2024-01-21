class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        given a list money in each house
        find max money you can take
        """
        
        # we want to find at each house, should the thief take the money or no
        # decide this and record the resulting amount take or not take
        # [1,2,3,1]
        # rob house 0 -> money is 1; not rob house 0 -> money is 0
        # rob house 1 -> not possible; rob house 1 -> money 2
        # rob house 2 ->
        # index is the house not touched yet
        n = len(nums)

        def rob(index, nums, memo):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            
            rob_curr = rob(index+2, nums, memo)
            not_rob_curr = rob(index+1, nums, memo)
            memo[index] = max(rob_curr+nums[index], not_rob_curr)
            return memo[index]
                
        return rob(0,nums, {})