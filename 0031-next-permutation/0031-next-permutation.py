class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums, start):
            i = start
            j = len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        i = len(nums)-2 # pivot. first index i from the back of the given array where arr[i] becomes smaller than arr[i+1].
        # find break
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1:
            # at last permutation
            # so next permutation is the one in increasing order(start)
            reverse(nums, 0)
        else:
            # have breakpoint
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            # reverse right half
            reverse(nums, i+1)