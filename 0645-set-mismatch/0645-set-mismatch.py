class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        dup = 0
        miss = 0
        for i in range(len(nums)+1):
            if i in s:
                if s[i] == 2:
                    dup = i
            else:
                miss = i
        return [dup, miss]