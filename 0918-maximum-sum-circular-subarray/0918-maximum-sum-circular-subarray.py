class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        input: nums: List[int] circular
        output: max sum of nonempty subarray(cannot reuse one element) of nums
        
        nums = [1,-2,3,-2] subarray [3]
        
        brute force: create all subarrays possible and get max sum
        kadane
        """
        global_max, global_min = nums[0], nums[0] # avoid case like negatives
        curr_max, curr_min = 0, 0
        n = len(nums)
        curr_sum = 0
        total = 0
        
        for i in range(n):
            # compare curr_sum, sum(nums[:i]), and nums[i]
            curr_max = max(curr_max+nums[i], nums[i])
            curr_min = min(curr_min+nums[i], nums[i])
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
            total += nums[i]
        if global_max < 0:
            return max(nums)
        leftover = total - global_min
        return max(leftover, global_max)
            
        