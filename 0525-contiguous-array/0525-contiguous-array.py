class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # prefix sum
        # arr only contains 0 and 1, if we treat 0 as -1, we are trying to find max len arr with sum == 0
        # we can use prefix sum and create a prefix sum arr, max len here
        
        # [0,1,0,1,1]
        # [0,0,1,1,2,3] 0
        # [0,-1,0,-1,0,1] -1
        
        n = len(nums)
        prefix_sum = [0] * (n+1)
        prefix_sum[0] = 0
        res = 0
        val_idx = {}
        
        #calc presum
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i]+ (-1 if nums[i] == 0 else 1)
        print(prefix_sum)
            
        # fill val to index for mapping presum at i to i
        for i in range(n+1):
            if prefix_sum[i] not in val_idx:
                val_idx[prefix_sum[i]] = i
            else:
                res = max(res, i - val_idx[prefix_sum[i]])
        return res