class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # absolute difference sum can be split into two parts:
        # left sum before i
        # right sum after i
        left_sum, right_sum = 0, sum(nums)-nums[0]
        res = []
        for i, num in enumerate(nums):
            left_diff_total = abs(num * i - left_sum)
            right_diff_total = abs(right_sum - num*(len(nums)-i-1))
            res.append(left_diff_total+right_diff_total)
            left_sum += nums[i]
            right_sum -= nums[i+1] if i < len(nums)-1 else 0
        return res
            
        