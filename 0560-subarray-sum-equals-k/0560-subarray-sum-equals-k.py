class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        total, count = 0,0
        
        for num in nums:
            total += num
            
            sub = total - k
            if sub in freq:
                count += freq[sub]
            if total not in freq:
                freq[total] = 0
            freq[total] += 1
        return count
                
            