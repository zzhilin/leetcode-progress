class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count of elements in nums
        # if any not divisible by 2 or 3 return -1
        # 2: 4, 3:3, 4:2
        cnt = Counter(nums)
        
        res = 0
        for c in cnt.values():
            if c == 1:
                return -1
            else:
                res += ceil(c / 3)
        return res
            