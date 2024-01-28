class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1

        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                
                slow += 1
                nums[slow] = nums[fast]
            fast += 1         
                
        return slow+1
