class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, val in enumerate(citations):
            if i >= val:
                return h
            h += 1
        return h