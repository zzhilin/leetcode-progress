class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = decreasing = True

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] - nums[i-1] < 0:
                decreasing = False
                
            if nums[i] - nums[i-1] > 0:
                increasing = False
            
            
        return increasing or decreasing
        