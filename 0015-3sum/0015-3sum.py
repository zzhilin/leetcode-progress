class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        approach
        sort
        fix 1 number using for loop
        two pointers for the numbers
        '''
        
        def two_sum(nums,target,first):
            i = 0
            j = len(nums)-1
            
            while i < j:
                total = first + nums[i] + nums[j]
                if total > target:
                    j -= 1
                elif total < target:
                    i += 1
                elif total == target:
                    res.append([first, nums[i], nums[j]])
                    i += 1
                    j-=1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                        
        res = []
        nums.sort()
        for i in range(len(nums)):
            curr = nums[i]
            if i == 0 or nums[i-1] != nums[i]:
                two_sum(nums[i+1:],0,curr)
        return res