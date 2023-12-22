class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = Counter(nums)
        nums[:freq[0]+1] = [0]*freq[0]
        nums[freq[0]:freq[0]+freq[1]] = [1]*freq[1]
        nums[freq[0]+freq[1]:] = [2]*freq[2]