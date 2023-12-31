from itertools import combinations
import sys

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        n = len(nums)
        # Step 1: Sort the array
        nums.sort()

        def find(level):
            i = 0
            cnt = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= level:
                    cnt += 1
                    i += 1
                i += 1
            return cnt
        left = 0
        right = nums[n-1] - nums[0]
        while left < right:
            mid = left+(right-left) // 2
            pairs=find(mid)
            if pairs >= p:
                right = mid
            else:
                left = mid+1
        return left


