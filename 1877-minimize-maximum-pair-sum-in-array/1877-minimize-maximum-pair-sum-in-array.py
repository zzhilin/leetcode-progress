class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0, len(nums)-1
        max_pair_sum = 0
        while i<j:

            curr_sum = nums[i] + nums[j]
            max_pair_sum = max(curr_sum, max_pair_sum)
            i += 1
            j -= 1
        return max_pair_sum