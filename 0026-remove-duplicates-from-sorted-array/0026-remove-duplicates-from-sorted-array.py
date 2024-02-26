class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        insert_at = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[insert_at] = nums[i]
                insert_at += 1
        return insert_at