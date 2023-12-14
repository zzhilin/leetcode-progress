class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        left, max_freq, total = 0,0,0
        for right in range(len(nums)):
            total += nums[right]
            # print(f"left is {left}, right is {right}, total is {total}")
            
            while nums[right]*(right-left+1) - total > k:
                total -= nums[left]
                left += 1
            
            max_freq = max(max_freq, right-left+1)
        return max_freq