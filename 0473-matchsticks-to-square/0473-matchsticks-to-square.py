class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        input: int list of diff length
        unknown: can we use all numbers only once to have one square
        """
        if sum(matchsticks) % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        side_sum = [0,0,0,0]
        def split(target_sum, curr_i,side_sum):
            if curr_i == len(matchsticks):
                return all(side == target_sum for side in side_sum)
            for i in range(4):
                if side_sum[i] + matchsticks[curr_i] <= target_sum:
                    side_sum[i]+=matchsticks[curr_i]
                    if split(target_sum, curr_i+1,side_sum):
                        return True
                    side_sum[i]-=matchsticks[curr_i]
            return False
        
        target = sum(matchsticks)//4
        return split(target, 0, side_sum)
                