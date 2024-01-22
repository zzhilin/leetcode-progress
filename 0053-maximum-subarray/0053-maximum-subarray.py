class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        input int arr
        return sum of largest subarr
        
        can we assume arr contain both pos and negative
        is arr going to be empty
        
        how big is the number, what is the range
        
        [1,2,3,-4]
        subarr len 1
        subarr len 2 [1,2] [2,3] [3,-4]
        len 3 [1,2,3] [2,3,-4]
        len 4
        return 6
        
        we want to know where optimal subarr begins
        use an int o kepp the curr sum, when the sum is negative, we can start with a new subarr
        
        '''
        max_subarr, curr = nums[0], nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i], nums[i]+curr)
                
            max_subarr = max(max_subarr, curr)
        return max_subarr