class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == len(set(nums)):
            return [nums]
        nums.sort()
        
        
        freq = Counter(nums)
        first = freq.most_common(1)[0]
        res = [[first[0]] for _ in range(first[1])]
        
        lst = freq.most_common()[1:]
        for pair in lst:
            for i in range(pair[1]):
                if pair[0] not in res[i]:
                    res[i].append(pair[0])
        
        
        return res