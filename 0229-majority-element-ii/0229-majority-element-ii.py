class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)//3
        res = []
        freq = Counter(nums)
        for num, f in freq.items():
            if f > threshold:
                res.append(num)
        return res