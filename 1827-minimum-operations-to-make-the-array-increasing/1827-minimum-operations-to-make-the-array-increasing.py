class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        1,5,2,4,1
        +4
        +3
        +7
        '''
        if len(nums) < 2:
            return 0
        # is next number larger than curr
        # if it is continue
        # if not increase so it's 1 larger than curr
        i = 0
        j = 1
        res = 0
        while j < len(nums):
            if nums[j] > nums[i]:
                j += 1
                i += 1
                continue
            else:
                diff = nums[i]-nums[j]
                nums[j] += (diff+1)
                res += (diff+1)
                j += 1
                i += 1
        return res