class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # traverse backwards
        res = [len(heights)-1]
        curr_max = heights[-1]
        for i in range(len(heights)-2, -1, -1):
            if curr_max < heights[i]:
                res.append(i)
                curr_max = heights[i]
        return sorted(res)
            