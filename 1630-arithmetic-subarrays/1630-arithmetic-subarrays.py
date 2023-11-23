class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        nums[4,6,5,9,3,7]
        l[0,0,2]
        r[2,3,5]
        
        0th [0,2] -> [4,6,5] [6,5,4]
        1th [0,3] -> [4,6,5,9]
        2th [2,5] -> [5,9,3,7]
        """
        # bf n^2
        # Function that checks if an arr is arithmetic
            # calc diff between first and second element
            # iterate over arr from 2nd element and compare diff
            # if different, return false
        def is_arithmetic(nums):
            diff = nums[1] - nums[0]
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] != diff:
                    return False
            return True
            
        # for range in l,r, get section of nums, sort, compare
        res = []
        for i, j in zip(l, r):
            # print(i,j)
            curr = sorted(nums[i:j+1], reverse=True)
            res.append(is_arithmetic(curr))
        return res
            
            