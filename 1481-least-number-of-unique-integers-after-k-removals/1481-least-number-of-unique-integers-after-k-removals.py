class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # SORT, remove least count numbers within k moves
        freq = Counter(arr)
        min_h = []
        for key,v in freq.items():
            heapq.heappush(min_h, (v,key))
        while k>0:
            curr = heapq.heappop(min_h)
            k -= 1
            freq[curr[1]] -= 1
            if freq[curr[1]]:
                heapq.heappush(min_h,(freq[curr[1]],curr[1]))
        # res = 0
        return len(min_h)
        
        
        