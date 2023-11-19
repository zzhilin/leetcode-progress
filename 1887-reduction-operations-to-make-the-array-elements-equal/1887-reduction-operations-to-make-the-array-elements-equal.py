class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        unique = sorted(cnts.keys(), reverse=True)
        ops = 0
        count = 0
        for i in range(len(unique)-1):
            count += cnts[unique[i]]
            ops += count
        return ops