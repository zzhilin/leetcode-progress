class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # brute
        # check if curr element is == prev element and after element
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            elif i == len(nums)-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    return nums[i]
                