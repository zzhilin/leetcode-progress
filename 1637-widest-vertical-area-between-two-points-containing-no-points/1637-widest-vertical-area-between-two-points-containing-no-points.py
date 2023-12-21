class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 1, 3, 5, 8, 9
        points.sort(key=lambda x: x[0])
        res = 0
        for i in range(1, len(points)):
            cur = points[i][0] - points[i-1][0]
            if cur > res:
                res = cur
        return res