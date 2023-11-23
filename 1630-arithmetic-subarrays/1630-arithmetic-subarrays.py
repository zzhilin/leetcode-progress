class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # diff = (max in arr - min in arr) / (n - 1)
        # we have n - 1 iteration between min and max, each increase by diff if it's arithmetic. total increased with diff * (n-1)
        # if diff is not an integer, than it's not arithmetic
        # if it is, min + diff must be in arr, every min + k * diff less than max is in arr.
        # if all are in arr, than it is arithmetic
        # convert arr to set for O(1) checks
        
        def check(nums):
            
            minimum = min(nums)
            maximum = max(nums)
            diff = (maximum-minimum) / (len(nums)-1)
            num_set = set(nums)
            if (maximum-minimum) % (len(nums)-1) != 0:
                return False
            curr = minimum + diff
            while curr < maximum:
                if curr not in num_set:
                    return False
                curr += diff
            return True
        res = []
        for i in range(len(l)):
            curr = nums[l[i]:r[i]+1]
            res.append(check(curr))
        return res
            
                
                
            
                