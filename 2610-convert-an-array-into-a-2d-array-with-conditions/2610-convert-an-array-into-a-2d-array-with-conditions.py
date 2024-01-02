class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums)+1)
        res = []
        
        for c in nums:
            if freq[c] >= len(res):
                res.append([])
            res[freq[c]].append(c)
            freq[c] += 1
        return res
                