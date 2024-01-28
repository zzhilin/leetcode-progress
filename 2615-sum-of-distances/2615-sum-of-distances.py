class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        indices = defaultdict(list)
        for i,val in enumerate(nums):
            indices[val].append(i)
            
        # print(indices)
        res = [0]*len(nums)
        
        
        for vals in indices.values():
            n = len(vals)
            prefix = list(accumulate(vals, initial=0))
            for i, target in enumerate(vals):
                left = target * i - prefix[i] # cur index * number of index before cur - prefix sum before curr
                right = prefix[n] - prefix[i] - target * (n - i) 
                res[target] = left+right
        return res