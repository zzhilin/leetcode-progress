class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_s = 0
        while l < r:
            s = 0
            if height[l] < height[r]:
                s = (r - l) * height[l]
                l += 1
            else:
                s = (r - l) * height[r]
                r -= 1
            max_s = max(s, max_s)
        return max_s