class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r= 0, n-1
        count = 0
        nums.sort()
        
        while l < r:
            if nums[l] + nums[r] < target:
                # sorted so all numbers between l and r has sum < target
                count += r - l
                l += 1
            else:
                r -= 1
        return count