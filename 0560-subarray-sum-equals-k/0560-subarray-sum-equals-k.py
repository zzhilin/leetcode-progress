class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sums = {0:1}
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in sums:
                
                cnt = cnt + sums[curr_sum-k]
            if curr_sum not in sums:
                sums[curr_sum] = 1
            else:
                sums[curr_sum] = sums[curr_sum]+1
        return cnt
        